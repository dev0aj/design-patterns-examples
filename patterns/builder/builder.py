from abc import ABC, abstractmethod
from typing import override

from patterns.builder.product import Product, Product1, Product2


class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> Product:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    @override
    def product(self) -> Product:
        product = self._product
        self.reset()
        return product

    @override
    def produce_part_a(self) -> None:
        self._product.add("PartA")

    @override
    def produce_part_b(self) -> None:
        self._product.add("PartB")

    @override
    def produce_part_c(self) -> None:
        self._product.add("PartC")


class ConcreteBuilder2(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product2()

    @property
    @override
    def product(self) -> Product:
        product = self._product
        self.reset()
        return product

    @override
    def produce_part_a(self) -> None:
        self._product.create("PartA")

    @override
    def produce_part_b(self) -> None:
        self._product.create("PartB")

    @override
    def produce_part_c(self) -> None:
        self._product.create("PartC")
