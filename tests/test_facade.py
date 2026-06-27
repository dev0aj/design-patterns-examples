import logging

from patterns.structural.facade.main import Facade, SubSystem1, SubSystem2

_logger = logging.getLogger(__name__)


def client_code(facade: Facade) -> None:

    _logger.info("%s", facade.operation())


def main() -> None:
    s1 = SubSystem1()
    s2 = SubSystem2()

    facade = Facade(s1, s2)
    client_code(facade)
