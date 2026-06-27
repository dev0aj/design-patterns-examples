import logging

from patterns.behavioral.command.command import Command, ComplexCommand, SimpleCommand
from patterns.behavioral.command.receiver import Receiver

_logger = logging.getLogger(__name__)


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command) -> None:
        self._on_start = command

    def set_on_finish(self, command: Command) -> None:
        self._on_start = command

    def do_something(self) -> None:
        _logger.info("Invoker: Before start")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        _logger.info("Invoker: Doing something.")

        _logger.info("Invoker: After finish")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


def main() -> None:
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say, Hi!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(receiver, "Send Email", "Save Report"))

    invoker.do_something()
