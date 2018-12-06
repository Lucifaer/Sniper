from core.MsgHandler import CheckMsg
from config import client_id, client_key
import aiohttp


class Authorization(object):
    def __init__(self, authorization_code):
        self.oauth2_endpoint = 'https://api.dropboxapi.com/oauth2/token'
        self.log = CheckMsg()
        self.authorization_code = authorization_code

    async def get_token(self):
        data = {
            'code': self.authorization_code,
            'grant_type': "authorization_code",
        }

        is_proxy = self.log.proxy_warning()

        async with aiohttp.ClientSession(auth=aiohttp.BasicAuth(client_id, client_key)) as session:
            if is_proxy == "":
                async with session.post(self.oauth2_endpoint, data=data, timeout=aiohttp.ClientTimeout(total=5)) as response:
                    return await response.text()
            else:
                async with session.post(self.oauth2_endpoint, data=data, timeout=aiohttp.ClientTimeout(total=5),
                                        proxy=is_proxy) as response:
                    return await response.text()
