import logging

from patterns.creational.factory.creator import ConcreteCreator1, ConcreteCreator2, Creator

logger = logging.getLogger(__name__)


ONE = 1
TWO = 2


class Config:
    version = ONE


class Application:
    def __init__(self, creator: Creator) -> None:
        self.creator = creator

    def run(self) -> None:
        logger.info("Client: I'm not aware of the creator's class, but it still works:")
        logger.info("%s", self.creator.some_operation())


class ApplicationCreator:
    def create(self, config: Config) -> Application:
        if config.version == ONE:
            creator = ConcreteCreator1()
        elif config.version == TWO:
            creator = ConcreteCreator2()
        else:
            msg = f"config version {config.version} is incompatible"
            raise ValueError(msg)
        return Application(creator)


def main() -> None:
    config = Config()
    app = ApplicationCreator().create(config)
    app.run()


if __name__ == "__main__":
    main()
