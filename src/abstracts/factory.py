from abc import ABC, abstractmethod
from .command import Command


class CommandFactory(ABC):
    @abstractmethod
    def get(self) -> Command:
        """creates a get Command"""

    @abstractmethod
    def store(self) -> Command:
        """creates a store Command"""

    @abstractmethod
    def dir(self) -> Command:
        """creates a dir Command"""

    @abstractmethod
    def lstdir(self) -> Command:
        """creates a lstdir Command"""

    @abstractmethod
    def mkdir(self) -> Command:
        """creates a mkdir Command"""
