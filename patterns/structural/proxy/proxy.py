import logging

from patterns.structural.proxy.subject import RealSubject, Subject

_logger = logging.getLogger(__name__)


class Proxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        if self._check_access():
            self._real_subject.request()
            self._log_access()

    def _check_access(self) -> bool:
        _logger.info("Proxy: Checking access prior to firing real request.")
        return True

    def _log_access(self) -> None:
        _logger.info("Proxy: Logging the time of request.")
