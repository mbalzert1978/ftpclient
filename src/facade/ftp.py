import ftplib
from pathlib import Path
from ..config.ftpconfig import FTPConfig


class FTPGetter:
    def __init__(self, config: FTPConfig) -> None:
        self.client = ftplib.FTP(config.host, config.user, config.password)

    def execute(self, remotefile: Path, localfile: Path) -> str:
        start = 0 if not remotefile.is_absolute() else 1
        end = len(remotefile.parts) if not remotefile.suffix else -1
        for folder in remotefile.parts[start:end]:
            self.client.cwd(folder)
        with localfile.open("rb") as local:
            return self.client.retrbinary(
                "RETR %s" % remotefile.name, local.write
            )
