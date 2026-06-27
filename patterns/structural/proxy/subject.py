import logging
from abc import ABC, abstractmethod

_logger = logging.getLogger(__name__)


class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):
    def request(self) -> None:
        _logger.info("RealSubject: Handling Request.")
