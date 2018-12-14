from core.Worker.base import Base
from core.DropBox.sharing import Sharing
from config import TEAM_OWNER_AUTHORIZATION_CODE, SHARING_DOCUMENT_ID, SHARING_DOCUMENT_ROOT
from pprint import pprint


class SharingWorker(Base):
    async def work(self, authorization_token, mod, args):
        mod_switch = await self.pre_check(mod)
        self.log.detail_info("Start sharing")
        sharing = Sharing(authorization_token=authorization_token)
        if mod_switch[0] == "team_owner":
            if mod_switch[1] == "add_folder_member":
                return await sharing.add_folder_member(SHARING_DOCUMENT_ID, args['members'], args['custom_message'])
            elif mod_switch[1] == "share_folder":
                return await sharing.share_folder(args['path'])

        elif mod_switch[0] == "team_member":
            if mod_switch[1] == "add_file_member":
                return await sharing.add_file_member(SHARING_DOCUMENT_ROOT + args['file'],
                                                     args['members'], args['custom_message'])
            elif mod_switch[1] == "create_shared_link":
                return await sharing.create_shared_link_with_settings(SHARING_DOCUMENT_ROOT + args['path'])

        else:
            self.log.error_then("Sniper only have three mod to share files:")
            self.log.error_then("1. team_owner")
            self.log.error_then("2. team_member")
            self.log.error_info(f"There\'s no mod called {mod_switch[0]}, please check your code!")

    async def pre_check(self, mod):
        mod_switch = mod.split('.')
        if len(mod_switch) != 2:
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
