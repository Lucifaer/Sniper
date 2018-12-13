from core.MsgHandler import LogHandler


class Base(object):
    def __init__(self):
        self.log = LogHandler()
