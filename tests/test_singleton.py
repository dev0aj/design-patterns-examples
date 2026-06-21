import logging
from threading import Thread

from patterns.singleton.singleton_meta import Singleton

logger = logging.getLogger(__name__)


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    logger.info("process value: %s, singleton value: %s", value, singleton.value)


def main() -> None:
    process1 = Thread(target=test_singleton, args=["FOO"])
    process2 = Thread(target=test_singleton, args=["BAR"])

    process1.start()
    process2.start()


if __name__ == "__main__":
    main()
