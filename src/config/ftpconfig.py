import os
from .ftptype import FTPType


class FTPConfig:
    def __init__(
        self, host, user, password=None, port=None, ftp_type=None
    ) -> None:
        self.host = host
        self.user = user
        self.password = password or os.getenv("ENV_PW")
        self.ftp_type = ftp_type or FTPType.FTP
        self.ftp_port = self.set_port(port)

    def set_port(self, value):
        return value if value else self.ftp_type.value
