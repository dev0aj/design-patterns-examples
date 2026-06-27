import logging

_logger = logging.getLogger(__name__)


class Receiver:
    def do_something(self, a: str) -> None:
        _logger.info("Receiver: Working on (%s)", a)

    def do_something_else(self, b: str) -> None:
        _logger.info("Receiver: Working on (%s)", b)
