import logging

from patterns.creational.abstract_factory.factory import AbstractFactory, ConcreteFactory1, ConcreteFactory2

logger = logging.getLogger(__name__)

ONE = 1
TWO = 2


class Config:
    version = TWO


class Application:
    def __init__(self, factory: AbstractFactory) -> None:
        self.factory = factory

    def run(self) -> None:
        product_a = self.factory.create_product_a()
        product_b = self.factory.create_product_b()

        logger.info("%s", product_b.operation_b())
        logger.info("%s", product_b.another_operation_b(product_a))


class ApplicationCreator:
    def create(self, config: Config) -> Application:
        if config.version == ONE:
            factory = ConcreteFactory1()
        elif config.version == TWO:
            factory = ConcreteFactory2()
        else:
            msg = f"config version {config.version} is incompatible"
            raise ValueError(msg)
        return Application(factory)


def main() -> None:
    config = Config()
    app = ApplicationCreator().create(config)
    app.run()


if __name__ == "__main__":
    main()
