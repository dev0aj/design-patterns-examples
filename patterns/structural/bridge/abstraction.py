from patterns.structural.bridge.implementation import Implementation


class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return f"Abstraction: Base operation with {self.implementation.operation_implementation()}"


class ExtendedAbstraction(Abstraction):
    """
    You can extend the Abstraction without changing the Implementation classes.
    """

    def operation(self) -> str:
        return f"ExtendedAbstraction: Extended operation with: {self.implementation.operation_implementation()}"
