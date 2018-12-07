from core.MsgHandler import LogHandler
from plugin.scroll_page import scroll_page
from pyppeteer import launch
import time


class Spider(object):
    def __init__(self):
        self.log = LogHandler()
        self.set_view_port_option = {
            'width': 1920,
            'height': 1080
        }
        self.goto_option = {
            'waitUntil': 'networkidle2',
        }
        self.pdf_option = {
            'width': 1920,
            'height': 1080,
            'format': 'A4',
        }

    async def spider(self, url):
        self.log.detail_info(f"[*] Start crawl {url}")
        self.log.detail_info(f"[*] {url} started at {time.strftime('%X')}")
        # Handle Error: pyppeteer.errors.NetworkError: Protocol error Runtime.callFunctionOn: Target closed.
        # Issue fix #1 by C1tas
        try:
            browser = await launch()
            page = await browser.newPage()
            await page.setViewport(self.set_view_port_option)
            await page.goto(url, self.goto_option)
            await scroll_page(page)
            pdf = await page.pdf(self.pdf_option)
            title = await page.title()
            filename = await self.translate_word(title)
            await browser.close()
            self.log.detail_info(f"[*] {url} finished at {time.strftime('%X')}")
            return filename, pdf
        except Exception as exc:
            self.log.error_then(f"[-] Occur an unexcepted error when crawl {url}: {str(exc)}!")
            self.log.detail_info(f"[*] {url} finished at {time.strftime('%X')}")
        finally:
            await browser.close()

    @staticmethod
    async def translate_word(word):
        table = {ord(f): ord(t) for f, t in zip(
            u'，。！？【】（）/％＃＠＆１２３４５６７８９０',
            u',.!?[]()-%#@&1234567890')}
        return word.translate(table)
