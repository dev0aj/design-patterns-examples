import logging

from patterns.structural.decorator.component import Component, ConcreteComponent
from patterns.structural.decorator.decorator import ConcreteDecoratorA

logger = logging.getLogger()


def client_code(component: Component) -> None:
    logger.info("%s", component.operation())


def main() -> None:
    simple = ConcreteComponent()

    logger.info("---------- Simple Component")
    client_code(simple)

    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorA(decorator1)
    logger.info("---------- Decorated Component")
    client_code(decorator2)
