import logging

from patterns.behavioral.chain_of_responsibility.handler import DogHandler, Handler, MonkeyHandler, SquirrelHandler

_logger = logging.getLogger(__name__)


def client_code(handler: Handler) -> None:

    for food in ["Nut", "Banana", "MeatBall"]:
        _logger.info("Client: Who wants a %s?", food)
        result = handler.handle(food)
        if result:
            _logger.info("---- %s", result)
        else:
            _logger.info("---- Food was left untouched")


def main() -> None:
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    _logger.info("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)

    _logger.info("-" * 50)
    _logger.info("SubChain: Monkey > Squirrel > Dog")
    client_code(squirrel)
