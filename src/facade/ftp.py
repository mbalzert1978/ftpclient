from __future__ import annotations

import ftplib
from pathlib import Path
from typing import TYPE_CHECKING

from ..config.ftpconfig import FTPConfig

if TYPE_CHECKING:
    import io


class NoDataError(Exception):
    def __init__(self, message: str, *args: object) -> None:
        super().__init__(message, *args)


class FTP:
    def __init__(self, config: FTPConfig) -> None:
        self.config = config
        self.client: ftplib.FTP = self.__create_client()

    def __create_client(self) -> ftplib.FTP:
        return ftplib.FTP()

    def __enter__(self) -> None:
        self.client.connect(host=self.config.host, port=self.config.ftp_port)
        self.client.login(user=self.config.user, passwd=self.config.password)

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        self.client.close()

    def load(
        self, file_name: str, file: io.BufferedReader = None
    ) -> io.BufferedReader:
        if file:
            return file
        resolve = Path(file_name).resolve()
        return resolve.open("rb")

    def save(
        self, file_name: str, file: io.BufferedWriter = None
    ) -> io.BufferedWriter:
        if file:
            return file
        resolve = Path(file_name).resolve()
        return resolve.open("wb")

    def put(self, file_name: str, file=None) -> str:
        file = file if file else self.load(file_name=file_name, file=file)
        data = self._put(file_name, file)
        return self.validate_result(data)

    def get(self, file_name: str, file=None) -> str:
        file = file if file else self.save(file_name=file_name, file=file)
        data = self._get(file_name, file)
        return self.validate_result(data)

    def validate_result(self, data: str) -> str:
        if data:
            return data
        raise NoDataError("No Data found.")

    def _put(self, file_name: str, file: io.BufferedReader) -> str:
        return self.client.storbinary(
            f"STOR {file_name}",
            file if file else self.load(file_name=file_name),
        )

    def _get(self, file_name: str, file: io.BufferedWriter) -> str:
        return self.client.retrbinary(
            f"RETR {file_name}",
            file.write if file else self.save(file_name=file_name).write,
        )
