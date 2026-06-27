class Facade:
    def __init__(self, subsystem1: SubSystem1, subsystem2: SubSystem2) -> None:
        self._subsystem1 = subsystem1
        self._subsystem2 = subsystem2

    def operation(self) -> str:
        results = []
        results.append("Facade initializes subsystems.")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action.")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class SubSystem1:
    def operation1(self) -> str:
        return "Subsystem1: Ready"

    def operation_n(self) -> str:
        return "Subsystem1: Go"


class SubSystem2:
    def operation1(self) -> str:
        return "Subsystem2: Ready"

    def operation_z(self) -> str:
        return "Subsystem2: Go"
