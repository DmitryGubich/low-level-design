from abc import ABC, abstractmethod


class Lockable(ABC):
    @abstractmethod
    def lock(self):
        pass

    @abstractmethod
    def unlock(self):
        pass


class NonLocking(Lockable):
    def lock(self):
        print("Door does not lock - ignoring")

    def unlock(self):
        print("Door cannot unlock because it cannot lock")


class Password(Lockable):
    def lock(self):
        print("Door locked using password!")

    def unlock(self):
        print("Door unlocked using password!")


class KeyCard(Lockable):
    def lock(self):
        pass

    def unlock(self):
        pass


class Openable(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass


class Standard(Openable):
    def open(self):
        print("Pushing door open")

    def close(self):
        print("Pulling door closed")


class Revolving(Openable):
    def open(self):
        pass

    def close(self):
        pass


class Sliding(Openable):
    def open(self):
        pass

    def close(self):
        pass
