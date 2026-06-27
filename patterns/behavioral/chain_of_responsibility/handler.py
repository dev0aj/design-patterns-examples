from abc import ABC, abstractmethod
from typing import Any


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request: Any) -> str | None:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler | None = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return self._next_handler

    @abstractmethod
    def handle(self, request: Any) -> str | None:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str | None:
        if request == "Banana":
            return f"Monkey: I will eat the {request}"
        return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str | None:
        if request == "Nut":
            return f"Squirrel: I will eat the {request}"
        return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str | None:
        if request == "MeatBall":
            return f"Dog: I will eat the {request}"
        return super().handle(request)
