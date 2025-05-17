from patterns.strategy.doors import ClosetDoor
from patterns.strategy.params import Standard, NonLocking, Password

if __name__ == "__main__":
    # Initialize door
    c = ClosetDoor()

    # Set behaviors
    c.set_open_behavior(Standard())
    c.set_lock_behavior(NonLocking())

    # Invoke behaviors
    c.perform_open()
    c.perform_close()
    c.perform_lock()
    c.perform_unlock()

    # Upgrade the door to be password protected
    c.set_lock_behavior(Password())
    c.perform_lock()
    c.perform_unlock()
