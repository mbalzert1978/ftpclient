from pathlib import Path
from src.facade.ftp import FTP
from src.config.ftpconfig import FTPConfig, FTPType


def main() -> None:
    config = FTPConfig(
        host="ftp.dlptest.com",
        user="dlpuser",
        password="rNrKYTX9g7z3RgJRmxWuGHbeu",
        ftp_type=FTPType.FTP,
    )
    client = FTP(config=config)
    local_file = Path.cwd() / "test.txt"
    with client.load("test.txt") as f:
        with client:
            result = client.put("new_test.txt", file=f)
    print(result)


if __name__ == "__main__":
    main()
