from core.Worker import CommonWorker
from core.MsgHandler import LogHandler
import asyncio
import time


class CommonTasks(object):
    def __init__(self):
        self.log = LogHandler()
        self.worker = CommonWorker()

    async def create_tasks(self, url, tag):
        authorization_token = await self.worker.get_token.work()
        if isinstance(url, str):
            spider_task = asyncio.create_task(self.worker.spider.work(url=url))
            file_name, pdf_buffer = await spider_task

            upload_task = asyncio.create_task(self.worker.upload.work(authorization_token, pdf_buffer,
                                                                      self.tag2path(tag, file_name)))
            await upload_task

    def tag2path(self, tag, file_name):
        return "/" + tag + "/" + file_name + ".pdf"

