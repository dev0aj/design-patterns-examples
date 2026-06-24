class Target:
    def request(self) -> str:
        return "Target: Default behaviour for Target."


class Adaptee:
    def specific_request(self) -> str:
        return ".eetpadA eht fo ruoivaheb laicepS"


class Adapter(Target, Adaptee):
    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"
