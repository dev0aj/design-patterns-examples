import logging

from patterns.structural.bridge.abstraction import Abstraction, ExtendedAbstraction
from patterns.structural.bridge.implementation import ConcreteImplementationA, ConcreteImplementationB

logger = logging.getLogger(__name__)


def client_code(abstraction: Abstraction) -> None:
    """
    Except for the initialization phase, where an Abstraction object gets linked
    with a specific Implementation object, the client code should only depend on
    the Abstraction class. This way the client code can support any abstraction-
    implementation combination.
    """

    # ...

    logger.info(abstraction.operation())

    # ...


def main() -> None:
    """
    The client code should be able to work with any pre-configured abstraction-
    implementation combination.
    """

    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    logger.info("-" * 50)

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)


if __name__ == "__main__":
    main()
