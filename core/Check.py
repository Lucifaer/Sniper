from core.Worker import Worker
from core.MsgHandler import LogHandler
import os
import json


class Check(object):
    def __init__(self):
        self.log = LogHandler()
        self.worker = Worker()

    async def check_authorization_code(self):
        if os.path.exists('authorization_code.json'):
            self.log.detail_info("[*] File: authorization_code.json is exist!")
            try:
                with open('authorization_code.json', 'r') as f:
                    token = json.load(f)
                if token['authorization'] != "":
                    self.log.success_info("[+] Success get authorization!")
                    return token['authorization']
                else:
                    self.log.error_then("[-] The authorization_code.json is not correct, deleting the file...")
            except Exception as exc:
                self.log.error_then("[-] The authorization_code.json is not correct, deleting the file...")
            try:
                os.remove('authorization_code.json')
                self.log.success_info("[+] Delete authorization_code.json successful!")
            except Exception as exc:
                self.log.error_info("[-] " + str(exc))
        else:
            self.log.error_then("[-] Not find authorization_code.json")
        return await self.worker.get_token_worker()
