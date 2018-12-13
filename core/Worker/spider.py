from core.Worker.base import Base
from core.Spider import Spider


class SpiderWorker(Base):
    async def work(self, url):
        url = await self.pre_check(url=url)
        spider = Spider()
        file_name, pdf_buffer = await spider.spider(url=url)
        self.log.success_info(f"{url} crawl successful.")
        return file_name, pdf_buffer

    async def pre_check(self, url):
        if url == "":
            self.log.error_info("You don\'t set an url to spider!")
        return url
