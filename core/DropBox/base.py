from core.MsgHandler import CheckMsg
import aiohttp
import json


class Base(object):
    def __init__(self, authorization_token):
        self.log = CheckMsg()
        self.token = authorization_token

    async def requests(self, endpoint, headers, data):
        is_proxy = self.log.proxy_warning()
        if isinstance(data, bytes):
            temp_data = data
        else:
            temp_data = json.dumps(data)

        async with aiohttp.ClientSession() as session:
            if is_proxy == "":
                async with session.post(endpoint, headers=headers, data=temp_data) as response:
                    return await response.text()
            else:
                async with session.post(endpoint, headers=headers, data=temp_data, proxy=is_proxy) as response:
                    return await response.text()
