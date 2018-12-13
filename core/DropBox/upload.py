from core.DropBox.base import Base
import aiohttp
import json


class Upload(Base):
    def __init__(self, authorization_token):
        super().__init__(authorization_token)
        self.upload_endpoint = 'https://content.dropboxapi.com/2/files/upload'

    async def upload(self, file_buffer, tag):
        upload_params = {
            'path': tag,
            'mode': "add",
            'autorename': True,
            'mute': False,
            'strict_conflict': False
        }

        headers = {
            'Authorization': self.token,
            'Content-Type': 'application/octet-stream',
            'Dropbox-API-Arg': json.dumps(upload_params),
        }

        return await self.requests(endpoint=self.upload_endpoint, headers=headers, data=file_buffer)
