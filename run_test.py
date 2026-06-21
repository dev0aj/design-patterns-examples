from argparse import ArgumentParser

from config.logger import setup_logging
from tests import test_abstract_factory, test_builder, test_factory, test_prototype, test_singleton

setup_logging()

PATTERN_RUNNERS = {
    "factory": test_factory.main,
    "abstract_factory": test_abstract_factory.main,
    "builder": test_builder.main,
    "prototype": test_prototype.main,
    "singleton": test_singleton.main,
}


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("pattern", help="name of the pattern to run", choices=list(PATTERN_RUNNERS.keys()))

    args = parser.parse_args()

    pattern = args.pattern

    method = PATTERN_RUNNERS.get(pattern)
    if method is None:
        msg = f"{pattern} is not a valid pattern name"
        raise ValueError(msg)

    method()


if __name__ == "__main__":
    main()
