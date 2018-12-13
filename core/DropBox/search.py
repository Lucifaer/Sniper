from core.DropBox.base import Base
import aiohttp
import json
from pprint import pprint


class Search(Base):
    def __init__(self, authorization_token):
        super().__init__(authorization_token)
        self.search_endpoint = 'https://api.dropboxapi.com/2/files/search'

    async def search(self, keyword):
        data = {
            'path': "",
            'query': keyword,
            'start': 0,
            'max_results': 100,
            'mode': "filename"
        }

        headers = {
            'Authorization': self.token,
            'Content-Type': "application/json",
        }

        is_proxy = self.log.proxy_warning()

        async with aiohttp.ClientSession() as session:
            if is_proxy == "":
                async with session.post(self.search_endpoint, headers=headers, data=data) as response:
                    return await response.text()
            else:
                async with session.post(self.search_endpoint, headers=headers, data=json.dumps(data), proxy=is_proxy) as response:
                    return pprint(await response.json())
