from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from patterns.behavioral.iterator.collection import WordsCollection


class AlphabeticalOrderIterator(Iterator):
    _position: int | None = None
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, *, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._sorted_items = None
        self._position = 0

    def __next__(self) -> Any:
        if not isinstance(self._position, int):
            msg = "Iterator not intialized."
            raise TypeError(msg)

        if self._sorted_items is None:
            self._sorted_items = sorted(self._collection._collection)  # noqa: SLF001
            if self._reverse:
                self._sorted_items = list(reversed(self._sorted_items))

        if self._position and self._position >= len(self._sorted_items):
            raise StopIteration

        value = self._sorted_items[self._position]
        self._position += 1
        return value
