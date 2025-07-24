import random
from abc import ABC, abstractmethod
from threading import Lock


class NoServersAvailableError(Exception):
    pass


class ServerSelectionStrategy(ABC):
    @abstractmethod
    def select_server(self, instance: list[str]) -> str:
        raise NotImplementedError()


class RoundRobinSelectionStrategy(ServerSelectionStrategy):
    def __init__(self):
        self.index = -1

    def select_server(self, instance: list[str]) -> str:
        if not len(instance):
            raise NoServersAvailableError()
        self.index = (self.index + 1) % len(instance)
        return instance[self.index]


class RandomSelectionStrategy(ServerSelectionStrategy):
    def select_server(self, instance: list[str]) -> str:
        if not len(instance):
            raise NoServersAvailableError()
        return random.choice(list(instance))


class LoadBalancer:
    def __init__(self, max_instances: int = 10, strategy: ServerSelectionStrategy | None = None):
        if max_instances <= 0:
            raise ValueError("Work with Positive Numbers Only")
        self.max_instances = max_instances
        self.instances = []
        self.lock = Lock()
        self.strategy = strategy if strategy else RoundRobinSelectionStrategy()

    def register(self, instance: str) -> bool:
        with self.lock:
            if len(self.instances) >= self.max_instances or instance in self.instances:
                return False
            self.instances.append(instance)
            return True

    def unregister(self, instance: str) -> bool:
        with self.lock:
            if instance not in self.instances:
                return False
            self.instances.remove(instance)
            return True

    def get(self) -> str:
        with self.lock:
            return self.strategy.select_server(self.instances)
