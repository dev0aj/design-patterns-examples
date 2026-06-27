import logging
from abc import ABC, abstractmethod

from patterns.behavioral.command.receiver import Receiver

_logger = logging.getLogger(__name__)


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    def __init__(self, payload: str) -> None:
        self._paylaod = payload

    def execute(self) -> None:
        _logger.info("SimpleCommand: Printing Payload")
        _logger.info("SimpleCommand: %s", self._paylaod)


class ComplexCommand(Command):
    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        _logger.info("ComplexCommand: Performed by the receiver")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)
