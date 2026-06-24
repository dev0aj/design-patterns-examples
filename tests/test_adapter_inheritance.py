import logging

from patterns.structural.adapter.inheritance.main import Adaptee, Adapter, Target

logger = logging.getLogger(__name__)


def client_code(target: Target) -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    logger.info("%s", target.request())


def main() -> None:
    logger.info("Client: I can work just fine with the Target objects:")
    target = Target()
    logger.info("calling client function...")
    client_code(target)
    logger.info("-" * 50)

    adaptee = Adaptee()
    logger.info("Client: The Adaptee class has a weird interface. See, I don't understand it:")
    msg = f"Adaptee: {adaptee.specific_request()}"
    logger.info("%s", msg)
    logger.info("-" * 50)

    logger.info("Client: But I can work with it via the Adapter:")
    logger.info("calling client function...")
    adapter = Adapter()
    client_code(adapter)


if __name__ == "__main__":
    main()
