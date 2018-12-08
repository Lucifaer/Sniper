from core.WorkerInterface import WorkerInterface
from core.DropBox.upload import Upload
import json


class UploadWorker(WorkerInterface):
    async def work(self, authorization_token, file_buffer, tag):
        file, path = await self.pre_check(file_buffer=file_buffer, tag=tag)
        self.log.detail_info("[*] Start upload files")
        uplaod = Upload(authorization_token=authorization_token)
        upload_json = json.loads(await uplaod.upload(file_buffer=file, tag=path))
        self.log.success_info(f"[+] File: {upload_json['name']} upload successful.")

    async def pre_check(self, file_buffer, tag):
        if file_buffer == "":
            self.log.error_info("[-] You don\'t have any file buffer to upload!")

        if tag == "":
            self.log.error_info("[-] You don\'t set an certain tag which confirm a path on dropbox!")

        return file_buffer, tag
