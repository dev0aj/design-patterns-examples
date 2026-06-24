import logging
from threading import Lock
from typing import Any, cast

logger = logging.getLogger(__name__)


class SingletonMeta(type):
    _instances: dict[type, object] = {}  # noqa: RUF012
    _lock: Lock = Lock()

    def __call__[T](cls: type[T], *args: Any, **kwargs: Any) -> T:
        with SingletonMeta._lock:
            if cls not in SingletonMeta._instances:
                SingletonMeta._instances[cls] = super().__call__(*args, **kwargs)

        return cast(T, SingletonMeta._instances[cls])


class Singleton(metaclass=SingletonMeta):
    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self) -> None:
        logger.info("some business logic")
