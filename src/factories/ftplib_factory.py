import ftplib

from ..abstracts.command import Command
from ..abstracts.factory import CommandFactory
from ..config.ftpconfig import FTPConfig


class ftplibCommandFactory(CommandFactory):
    def __init__(self, config: FTPConfig) -> None:
        self.client = ftplib.FTP(config.host, config.user, config.password)

    def get(self) -> Command:
        return super().get()
