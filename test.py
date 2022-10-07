from pathlib import Path
from src.config.ftpconfig import FTPConfig
from src.config.ftptype import FTPType
from src.facade.ftp import FTPGetter

config = FTPConfig(
    "ftp.dlptest.com", "dlpuser", "rNrKYTX9g7z3RgJRmxWuGHbeu", FTPType.FTP
)

get = FTPGetter(config)

get.execute(Path("upload.txt"), Path.cwd())
