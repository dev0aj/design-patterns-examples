from patterns.creational.builder.builder import Builder
from patterns.creational.builder.product import Product


class Director:
    def __init__(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> Product:
        self._builder.produce_part_a()
        return self._builder.product

    def build_full_featured_product(self) -> Product:
        self._builder.produce_part_a()
        self._builder.produce_part_b()
        self._builder.produce_part_c()
        return self._builder.product
