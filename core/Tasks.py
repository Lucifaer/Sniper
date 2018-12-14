from core.Worker import CommonWorker, InviteWorker
from core.MsgHandler import LogHandler
from config import TEAM_OWNER_AUTHORIZATION_CODE
import asyncio


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

            share_task = asyncio.create_task(self.worker.sharing.work(authorization_token,
                                                                      'team_member.create_shared_link',
                                                                      {'path': self.tag2path(tag, file_name)}))
            await share_task

    def tag2path(self, tag, file_name):
        return "/" + tag + "/" + file_name + ".pdf"


class InviteTasks(object):
    def __init__(self):
        self.worker = InviteWorker()

    async def create_tasks(self, invite_list):
        members = []
        with open(invite_list, 'rt') as f:
            for i in f:
                members.append(
                    {
                        "member": {
                            ".tag": "email",
                            "email": i
                        }
                    }
                )

        args = {
            'members': members,
            'custom_message': "test"
        }
        invite_task = asyncio.create_task(self.worker.sharing.work(TEAM_OWNER_AUTHORIZATION_CODE,
                                                                'team_owner.add_folder_member', args))
        await invite_task
