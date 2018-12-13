from core.WorkerInterface import WorkerInterface
from core.DropBox.sharing import Sharing
from config import TEAM_OWNER_AUTHORIZATION_CODE, SHARING_DOCUMENT_ID, SHARING_DOCUMENT_ROOT
import json


class SharingWorker(WorkerInterface):
    async def work(self):
        pass

    async def pre_check(self, mod, args):
        if mod == "personal":
            pass
        elif mod == "team_owner":
            if TEAM_OWNER_AUTHORIZATION_CODE == "":
                self.log.error_info("")
            else:
                self.log.detail_info("Start sharing to team document")
        elif mod == "team_member":
            if SHARING_DOCUMENT_ID == "":
                self.log.error_info("")
        else:
            self.log.error_then("Sniper only have two mod to share files:")
            self.log.error_then("1. personal")
            self.log.error_then("2. team")
            self.log.error_info(f"There\'s no mod called {mod}, please check your code!")



