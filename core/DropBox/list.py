from core.DropBox.base import Base
from pprint import pprint


class List(Base):
    def __init__(self, authorization_code):
        super().__init__(authorization_code)
        self.list_endpoint = 'https://api.dropboxapi.com/2/files/list_folder'

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

        return pprint(await self.requests(endpoint=self.list_endpoint, headers=headers, data=data))
