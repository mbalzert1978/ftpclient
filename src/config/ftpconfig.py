from dataclasses import dataclass, field

from .ftptype import FTPType


@dataclass
class FTPConfig:
    host: str
    user: str
    password: str
    ftp_type: FTPType
    port: int = field(default=0)

    def __post__init__(self) -> None:
        if self.port:
            return
        self.port = self.ftp_type.value
