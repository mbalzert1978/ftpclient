from abc import abstractmethod
import ftplib
from ..abstracts.command import Command


class ftplibCommand(Command):
    def __init__(self, client: ftplib.FTP) -> None:
        self.client = client

    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError


class get(ftplibCommand):
    def __init__(self, client: ftplib.FTP) -> None:
        super().__init__(client)

    def execute(self) -> None:
        return super().execute()
