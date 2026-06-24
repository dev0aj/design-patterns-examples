import logging

from patterns.structural.composite.component import Component, Composite, Leaf

logger = logging.getLogger(__name__)


def client_code(component: Component) -> None:
    logger.info("RESULT: %s", component.operation())


def client_code2(component1: Component, component2: Component) -> None:
    if component1.is_composite():
        component1.add(component2)
    logger.info("RESULT: %s", component1.operation())


def main() -> None:
    simple = Leaf()
    logger.info("----------- Simple Component")
    client_code(simple)

    logger.info("-" * 50)

    tree = Composite()
    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    logger.info("----------- Composite Component")
    client_code(tree)


if __name__ == "__main__":
    main()
