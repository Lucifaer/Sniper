from core.Worker import Worker
from core.Check import Check
from core.MsgHandler import LogHandler
import asyncio
import time


class CommonTasks(object):
    def __init__(self):
        self.log = LogHandler()
        self.worker = Worker()
        self.check = Check()

    async def create_tasks(self, url, tag):
        authorization_token = await self.check.check_authorization_code()
        if isinstance(url, str):
            spider_task = asyncio.create_task(self.worker.spider_worker(url))
            file_name, pdf_buffer = await spider_task

            upload_task = asyncio.create_task(self.worker.upload_worker(authorization_token, pdf_buffer,
                                                                        self.tag2path(tag, file_name)))
            await upload_task

    @staticmethod
    def tag2path(tag, file_name):
        return "/" + tag + "/" + file_name + ".pdf"

