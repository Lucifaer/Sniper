from core.Worker.get_token import GetTokenWorker
from core.Worker.spider import SpiderWorker
from core.Worker.upload import UploadWorker
from core.Worker.sharing import SharingWorker


class CommonWorker(object):
    def __init__(self):
        self.get_token = GetTokenWorker()
        self.spider = SpiderWorker()
        self.upload = UploadWorker()
        self.sharing = SharingWorker()

class InviteWorker(object):
    def __init__(self):
        self.sharing = SharingWorker()
