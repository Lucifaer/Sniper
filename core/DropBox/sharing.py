from core.DropBox.base import Base
from pprint import pprint


class Sharing(Base):
    def __init__(self, authorization_token):
        super().__init__(authorization_token)
        self.add_file_member_endpoint = 'https://api.dropboxapi.com/2/sharing/add_file_member'
        self.add_folder_member_endpoint = 'https://api.dropboxapi.com/2/sharing/add_folder_member'
        self.share_folder_endpoint = 'https://api.dropboxapi.com/2/sharing/share_folder'

    async def add_file_member(self, file, members, custom_message):
        data = {
            'file': file,
            'members': members,
            'custom_message': custom_message,
            'quiet': False,
            'access_level': "viewer",
            'add_message_as_comment': False
        }
        headers = {
            'Authorization': self.token,
            'Content-Type': "application/json",
        }

        return await self.requests(endpoint=self.add_file_member_endpoint, headers=headers, data=data)

    async def add_folder_member(self, shared_folder_id, members, custom_message):
        data = {
            'shared_folder_id': shared_folder_id,
            'members': members,
            'quiet': False,
            'custom_message': custom_message
        }
        headers = {
            'Authorization': self.token,
            'Content-Type': "application/json",
        }

        return pprint(await self.requests(endpoint=self.add_folder_member_endpoint, headers=headers, data=data))

    async def share_folder(self, path):
        data = {
            'path': path,
            'acl_update_policy': "owner",
            'force_async': False,
            'member_policy': "team",
            'access_inheritance': "inherit"
        }
        headers = {
            'Authorization': self.token,
            'Content-Type': "application/json",
        }

        return pprint(await self.requests(endpoint=self.share_folder_endpoint, headers=headers, data=data))
