import ftplib
from os import PathLike
from pathlib import Path
from ..config.ftpconfig import FTPConfig


class FTPGetter:
    def __init__(
        self, config: FTPConfig, remotefile: PathLike, localfile: PathLike
    ) -> None:
        self.client = ftplib.FTP(config.host, config.user, config.password)
        self.remotefile = Path(remotefile)
        self.localfile = Path(localfile)

    def execute(self) -> str:
        for folder in self.remotefile.parts[self.start() : self.end()]:
            self.client.cwd(folder)
        with self.localfile.open("wb") as local:
            return self.client.retrbinary(
                "RETR %s" % self.remotefile.name, local.write
            )

    def end(self) -> int:
        return len(self.remotefile.parts) if not self.remotefile.suffix else -1

    def start(self) -> int:
        return 0 if not self.remotefile.is_absolute() else 1
