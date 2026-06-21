import logging
from abc import ABC, abstractmethod
from typing import override

logger = logging.getLogger(__name__)


class Product(ABC):
    @abstractmethod
    def show(self) -> None:
        pass


class Product1(Product):
    def __init__(self) -> None:
        self.parts: list[str] = []

    def add(self, part: str) -> None:
        self.parts.append(part)

    @override
    def show(self) -> None:
        msg = f"Product1 parts: {', '.join(self.parts)}"
        logger.info("%s", msg)


class Product2(Product):
    def __init__(self) -> None:
        self.parts: list[str] = []

    def create(self, part: str) -> None:
        self.parts.append(part)

    @override
    def show(self) -> None:
        msg = f"Product2 parts: {', '.join(self.parts)}"
        logger.info("%s", msg)
