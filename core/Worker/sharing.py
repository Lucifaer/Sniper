from core.Worker.base import Base
from core.DropBox.sharing import Sharing
from config import TEAM_OWNER_AUTHORIZATION_CODE, SHARING_DOCUMENT_ID
from pprint import pprint


class SharingWorker(Base):
    async def work(self, authorization_token, mod, args):
        mod_switch = await self.pre_check(mod)
        self.log.detail_info("Start sharing")
        if authorization_token != TEAM_OWNER_AUTHORIZATION_CODE:
            if mod_switch[0] == "team_owner":
                sharing = Sharing(authorization_token=TEAM_OWNER_AUTHORIZATION_CODE)
            else:
                sharing = Sharing(authorization_token=authorization_token)

        if mod_switch[0] == "team_owner":
            if mod_switch[1] == "add_folder_member":
                for i in args['members']:
                    pprint(await sharing.add_folder_member(args['shared_folder_id'], i, args['custom_message']))
            elif mod_switch[1] == "share_folder":
                pprint(await sharing.share_folder(args['path']))

        elif mod_switch[0] == "team_member":
            for i in args['members']:
                pprint(await sharing.add_file_member(args['file'], i, args['custom_message']))

        else:
            self.log.error_then("Sniper only have three mod to share files:")
            self.log.error_then("1. team_owner")
            self.log.error_then("2. team_member")
            self.log.error_info(f"There\'s no mod called {mod_switch[0]}, please check your code!")

    async def pre_check(self, mod):
        mod_switch = mod.split('.')
        if len(mod_switch) > 2:
            self.log.error_info(f"There is no sharing mod name {mod}")
        if mod_switch[0] == "team_owner":
            if TEAM_OWNER_AUTHORIZATION_CODE == "":
                self.log.error_info("You have not set a team-owner-auth-code in config.py!")
            if SHARING_DOCUMENT_ID == "":
                self.log.error_info("You have not set a sharing document id in config.py")
        elif mod_switch[0] == "team_member":
            if SHARING_DOCUMENT_ID == "":
                self.log.error_info("You have not set a sharing document id in config.py")
        return mod_switch
