import copy
import logging

from patterns.prototype.component import SelfReferencingEntity, SomeComponent

logger = logging.getLogger(__name__)


def main() -> None:
    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()

    component = SomeComponent(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    shallow_copied_component = copy.copy(component)
    deep_copied_component = copy.deepcopy(component)

    logger.info("component")
    logger.info(component.some_list_of_objects)

    logger.info("shallow_copied_component")
    logger.info(shallow_copied_component.some_list_of_objects)

    logger.info("deep_copied_component")
    logger.info(deep_copied_component.some_list_of_objects)

    logger.info("-" * 50)

    logger.info("- adding object to 'some_list_of_objects' in shallow_copied_component")
    shallow_copied_component.some_list_of_objects.append("shallow copy object")

    logger.info("component")
    logger.info(component.some_list_of_objects)

    logger.info("shallow_copied_component")
    logger.info(shallow_copied_component.some_list_of_objects)

    logger.info("deep_copied_component")
    logger.info(deep_copied_component.some_list_of_objects)

    logger.info("- adding object to 'some_list_of_objects' in deep_copied_component")
    deep_copied_component.some_list_of_objects.append("deep copy object")

    logger.info("component")
    logger.info(component.some_list_of_objects)

    logger.info("shallow_copied_component")
    logger.info(shallow_copied_component.some_list_of_objects)

    logger.info("deep_copied_component")
    logger.info(deep_copied_component.some_list_of_objects)


if __name__ == "__main__":
    main()
