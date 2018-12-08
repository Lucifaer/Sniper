from core.WorkerInterface import WorkerInterface
from core.Spider import Spider


class SpiderWorker(WorkerInterface):
    async def work(self, url):
        url = await self.pre_check(url=url)
        spider = Spider()
        file_name, pdf_buffer = await spider.spider(url=url)
        self.log.success_info(f"[+] {url} crawl successful.")
        return file_name, pdf_buffer

    async def pre_check(self, url):
        if url == "":
            self.log.error_info("[-] You don\'t set an url to spider!")
        return url
