from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log_message(self, message: str) -> None:
        pass


class XmlLogger:
    def log(self, xml_message: str) -> None:
        print(xml_message)


class JsonLogger(Logger):
    def log_message(self, message: str) -> None:
        print(message)


class LoggerAdapter(Logger):
    def __init__(self, xml_logger: XmlLogger) -> None:
        self.xml_logger = xml_logger

    def log_message(self, message: str) -> None:
        self.xml_logger.log(message)
