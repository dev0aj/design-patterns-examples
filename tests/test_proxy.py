import logging

from patterns.structural.proxy.proxy import Proxy
from patterns.structural.proxy.subject import RealSubject, Subject

_logger = logging.getLogger(__name__)


def client_code(subject: Subject) -> None:

    subject.request()


def main() -> None:
    _logger.info("Client: Executing client code with a real subject.")
    real_subject = RealSubject()
    client_code(real_subject)

    _logger.info("Client: Executing client code with a proxy subject.")
    proxy = Proxy(real_subject)
    client_code(proxy)
