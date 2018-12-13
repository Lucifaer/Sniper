from core.Worker.base import Base
from core.DropBox.authorization import Authorization
from config import DROPBOX_AUTHORIZATION_CODE, client_id
import json
import os


class GetTokenWorker(Base):
    async def work(self):
        if os.path.exists('authorization_code.json'):
            self.log.detail_info("File: authorization_code.json is exist!")
            try:
                with open('authorization_code.json', 'r') as f:
                    token = json.load(f)
                if token['authorization'] != "":
                    self.log.success_info("Success get authorization!")
                    return token['authorization']
                else:
                    self.log.error_then("The authorization_code.json is not correct, deleting the file...")
            except Exception as exc:
                self.log.error_then(f"Occur an unexpected error when reading authorization_code.json: {str(exc)}")
                self.log.error_then("The authorization_code.json is not correct, deleting the file...")
            try:
                os.remove('authorization_code.json')
                self.log.success_info("Delete authorization_code.json successful!")
            except Exception as exc:
                self.log.error_info(f"Occur an unexpected error when removing authorization_code.json: {str(exc)}")
        else:
            self.log.error_then("Not find authorization_code.json")
        return await self.create_authorization()

    async def pre_check(self):
        if DROPBOX_AUTHORIZATION_CODE == "":
            self.log.error_info(f"You don\'t set DROPBOX_ACCESS_TOKEN in config.py,\n"
                                f"Please login https://www.DropBox.com/oauth2/authorize?"
                                f"client_id={client_id}&response_type=code "
                                f"to get an ACCESS_TOKEN")

    async def create_authorization(self):
        await self.pre_check()
        self.log.detail_info("Trying to get authorization-token information")
        authorization = Authorization(authorization_code=DROPBOX_AUTHORIZATION_CODE)
        try:
            token_json = json.loads(await authorization.get_token())
            token_json.setdefault('authorization',
                                  token_json['token_type'].capitalize() + " " + token_json['access_token'])
            with open('authorization_code.json', 'x') as f:
                json.dump(token_json, f)
            self.log.success_info("File: authorization_code.json created.")
            return token_json['authorization']
        except KeyError:
            self.log.error_info(f"Your DROPBOX_ACCESS_TOKEN in config.py has been used! "
                                f"Try another DROPBOX_ACCESS_TOKEN from https://www.DropBox.com/oauth2/authorize?"
                                f"client_id={client_id}&response_type=code")
