from core.DropBox.base import Base
import aiohttp
from config import client_id, client_key


class Authorization(Base):
    def __init__(self, authorization_code):
        super().__init__(authorization_code)
        self.oauth2_endpoint = 'https://api.dropboxapi.com/oauth2/token'

    async def get_token(self):
        data = {
            'code': self.token,
            'grant_type': "authorization_code",
        }
        headers = {
            'Content-Type': "application/json",
        }

        return await self.requests(endpoint=self.oauth2_endpoint, headers=headers, data=data)

    async def requests(self, endpoint, headers, data):
        is_proxy = self.log.proxy_warning()

        async with aiohttp.ClientSession(auth=aiohttp.BasicAuth(client_id, client_key)) as session:
            if is_proxy == "":
                async with session.post(self.oauth2_endpoint, data=data,
                                        timeout=aiohttp.ClientTimeout(total=5)) as response:
                    return await response.text()
            else:
                async with session.post(self.oauth2_endpoint, data=data, timeout=aiohttp.ClientTimeout(total=5),
                                        proxy=is_proxy) as response:
                    return await response.text()
