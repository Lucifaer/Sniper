from core.MsgHandler import CheckMsg
import aiohttp
import json


class Upload(object):
    def __init__(self, authorization_token):
        self.upload_endpoint = 'https://content.dropboxapi.com/2/files/upload'
        self.log = CheckMsg()
        self.token = authorization_token

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

        # data = {
        #     'file': file_buffer
        # }

        is_proxy = self.log.proxy_warning()

        async with aiohttp.ClientSession() as session:
            if is_proxy == "":
                async with session.post(self.upload_endpoint, headers=headers, data=file_buffer) as response:
                    return await response.text()
            else:
                async with session.post(self.upload_endpoint, headers=headers, data=file_buffer, proxy=is_proxy) as response:
                    return await response.text()
