from click import secho
from config import PROXY


class LogHandler(object):
    def __init__(self):
        self.success_fg = 'bright_green'
        self.warning_fg = 'yellow'
        self.error_fg = 'bright_red'
        self.detail_fg = 'bright_blue'

    def success_info(self, info):
        secho(f"[+] {info}", fg=self.success_fg)

    def warning_info(self, info):
        secho(f"[!] {info}", fg=self.warning_fg)

    def error_info(self, info):
        secho(f"[-] {info}", fg=self.error_fg)
        exit()

    def error_then(self, info):
        secho(f"[-] {info}", fg=self.error_fg)

    def detail_info(self, info):
        secho(f"[*] {info}", fg=self.detail_fg)


class CheckMsg(LogHandler):
    def proxy_warning(self):
        if PROXY == "":
            self.warning_info("Because of GFW, you may can't connect to http://api.DropBox.com, "
                              "so you'd better set a PROXY in config.py")
        else:
            self.detail_info(f"Set proxy {PROXY}")
        return PROXY
