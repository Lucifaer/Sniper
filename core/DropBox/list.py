from core.DropBox.base import Base
from pprint import pprint
import json


class List(Base):
    def __init__(self, authorization_code):
        super().__init__(authorization_code)
        self.list_endpoint = 'https://api.dropboxapi.com/2/files/list_folder'
        self.list_folders_continue_endpoint = 'https://api.dropboxapi.com/2/files/list_folder/continue'

    async def list_folder(self, path=""):
        data = {
            'path': path,
            'recursive': True,
            'include_media_info': False,
            'include_has_explicit_shared_members': True,
            'include_mounted_folders': True
        }
        headers = {
            'Authorization': self.token,
            'Content-Type': "application/json",
        }

        content = json.loads(await self.requests(endpoint=self.list_endpoint, headers=headers, data=data))
        pprint(content)
        pprint(content['has_more'])
        if content['has_more']:
            pprint(json.loads(await self.list_folder_continue(content['cursor'])))

    async def list_folder_continue(self, cursor):
        data = {
            'cursor': cursor
        }
        headers = {
            'Authorization': self.token,
            'Content-Type': "application/json",
        }
        return await self.requests(endpoint=self.list_folders_continue_endpoint, headers=headers, data=data)
