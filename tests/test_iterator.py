import logging

from patterns.behavioral.iterator.collection import WordsCollection

_logger = logging.getLogger(__name__)


def main() -> None:
    collection = WordsCollection()
    collection.add_item("B")
    collection.add_item("A")
    collection.add_item("C")

    _logger.info("Straight Traversal:")
    _logger.info("%s", ",".join(collection))

    _logger.info("-" * 50)

    _logger.info("Reverse Traversal:")
    _logger.info("%s", ",".join(collection.get_reverse_iterator()))
