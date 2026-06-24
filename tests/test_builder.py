import logging

from patterns.creational.builder.builder import Builder, ConcreteBuilder1, ConcreteBuilder2
from patterns.creational.builder.director import Director

logger = logging.getLogger(__name__)


ONE = 1
TWO = 2


class Config:
    version = ONE


class Application:
    def __init__(self, builder: Builder) -> None:
        self.builder = builder
        self.director = Director(builder)

    def run(self) -> None:
        logger.info("Standard basic product: ")
        basic_product = self.director.build_minimal_viable_product()
        basic_product.show()

        logger.info("")

        logger.info("Standard full featured product: ")
        full_product = self.director.build_full_featured_product()
        full_product.show()

        logger.info("")

        # Remember, the Builder pattern can be used without a Director class.
        logger.info("Custom product: ")
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        custom_product = self.builder.product
        custom_product.show()


class ApplicationCreator:
    def create(self, config: Config) -> Application:

        if config.version == ONE:
            builder = ConcreteBuilder1()
        elif config.version == TWO:
            builder = ConcreteBuilder2()
        else:
            msg = f"config version {config.version} is incompatible"
            raise ValueError(msg)
        return Application(builder)


def main() -> None:
    config = Config()
    app = ApplicationCreator().create(config)
    app.run()


if __name__ == "__main__":
    main()
