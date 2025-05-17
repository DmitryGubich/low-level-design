from abc import ABC


class Door(ABC):  # noqa: B024
    def __init__(self):
        # Using underscore as convention for private members in Python
        self._lock_behavior = None
        self._open_behavior = None

    def set_lock_behavior(self, lock_behavior):
        self._lock_behavior = lock_behavior

    def set_open_behavior(self, open_behavior):
        self._open_behavior = open_behavior

    def perform_lock(self):
        self._lock_behavior.lock()

    def perform_unlock(self):
        self._lock_behavior.unlock()

    def perform_open(self):
        self._open_behavior.open()

    def perform_close(self):
        self._open_behavior.close()

    def get_dimensions(self):
        return 5


class ClosetDoor(Door):
    pass


class ExternalDoor(Door):
    pass


class SafeDepositDoor(Door):
    pass


class SlidingDoor(Door):
    pass
