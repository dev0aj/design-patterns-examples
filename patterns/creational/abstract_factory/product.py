from abc import ABC, abstractmethod
from typing import override


class AbstractProductA(ABC):
    @abstractmethod
    def operation_a(self) -> str:
        pass


class ConcreteProductA1(AbstractProductA):
    @override
    def operation_a(self) -> str:
        return "Result of Product A1"


class ConcreteProductA2(AbstractProductA):
    @override
    def operation_a(self) -> str:
        return "Result of Product A2"


class AbstractProductB(ABC):
    @abstractmethod
    def operation_b(self) -> str:
        pass

    @abstractmethod
    def another_operation_b(self, collaborator: AbstractProductA) -> str:
        pass


class ConcreteProductB1(AbstractProductB):
    @override
    def operation_b(self) -> str:
        return "Result of Product B1"

    @override
    def another_operation_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.operation_a()
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    @override
    def operation_b(self) -> str:
        return "Result of Product B2"

    @override
    def another_operation_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.operation_a()
        return f"The result of the B2 collaborating with the ({result})"
