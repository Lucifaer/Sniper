from core.DropBox.authorization import Authorization
from core.DropBox.upload import Upload
from core.Spider import Spider
from core.MsgHandler import LogHandler
from config import DROPBOX_AUTHORIZATION_CODE, client_id
import json


class Worker(object):
    def __init__(self):
        self.log = LogHandler()

    async def get_token_worker(self):
        if DROPBOX_AUTHORIZATION_CODE == "":
            self.log.error_info(f"[-] You don\'t set DROPBOX_ACCESS_TOKEN in config.py,\n"
                                f"Please login https://www.DropBox.com/oauth2/authorize?"
                                f"client_id={client_id}&response_type=code "
                                f"to get an ACCESS_TOKEN")

        self.log.detail_info("[*] Trying to get authorization-token information")

        authorization = Authorization(authorization_code=DROPBOX_AUTHORIZATION_CODE)
        try:
            token_json = json.loads(await authorization.get_token())
            token_json.setdefault('authorization', token_json['token_type'].capitalize() + " " + token_json['access_token'])
            with open('authorization_code.json', 'x') as f:
                json.dump(token_json, f)
            self.log.success_info("[+] File: authorization_code.json created.")
            return token_json['authorization']
        except KeyError:
            self.log.error_info(f"[-] Your DROPBOX_ACCESS_TOKEN in config.py has been used! "
                                f"Try another DROPBOX_ACCESS_TOKEN from https://www.DropBox.com/oauth2/authorize?"
                                f"client_id={client_id}&response_type=code")

    async def upload_worker(self, authorization_token, file_buffer, tag):
        if file_buffer == "":
            self.log.error_info("[-] You don\'t have any file buffer to upload!")

        if tag == "":
            self.log.error_info("[-] You don\'t set an certain tag which confirm a path on dropbox!")

        self.log.detail_info("[*] Start upload files")

        uplaod = Upload(authorization_token=authorization_token)
        upload_json = json.loads(await uplaod.upload(file_buffer=file_buffer, tag=tag))
        self.log.success_info(f"[+] File: {upload_json['name']} upload successful.")

    async def spider_worker(self, url):
        if url == "":
            self.log.error_info("[-] You don\'t set an url to spider!")

        spider = Spider()
        file_name, pdf_buffer = await spider.spider(url)
        self.log.success_info(f"[+] {url} crawl successful.")
        return file_name, pdf_buffer
