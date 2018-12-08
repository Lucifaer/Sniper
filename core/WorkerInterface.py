from core.MsgHandler import LogHandler


class WorkerInterface(object):
    def __init__(self):
        self.log = LogHandler()
