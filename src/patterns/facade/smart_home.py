from enum import Enum


class Brightness(Enum):
    UNKNOWN = 0
    BRIGHT = 1
    DIM = 2


class Service(Enum):
    UNKNOWN = 0
    HULU = 1
    NETFLIX = 2
    HBO = 3


class SmartHomeSubSystem:
    def __init__(self):
        self.brightness = Brightness.UNKNOWN
        self.temperature = 19
        self.is_security_armed = False
        self.streaming_service = Service.UNKNOWN

    def set_brightness(self, brightness):
        self.brightness = brightness

    def set_temperature(self, temperature):
        self.temperature = temperature

    def set_is_security_armed(self, is_security_armed):
        self.is_security_armed = is_security_armed

    def set_streaming_service(self, streaming_service):
        self.streaming_service = streaming_service

    def __str__(self):
        return (
            f"Brightness: {self.brightness}\n"
            f"Temperature: {self.temperature}\n"
            f"Is security armed: {self.is_security_armed}\n"
            f"Streaming service: {self.streaming_service}"
        )


class SmartHomeFacade:
    def __init__(self, smart_home):
        self.smart_home = smart_home

    def set_movie_mode(self):
        self.smart_home.set_brightness(Brightness.DIM)
        self.smart_home.set_temperature(21)
        self.smart_home.set_is_security_armed(False)
        self.smart_home.set_streaming_service(Service.NETFLIX)

    def set_focus_mode(self):
        self.smart_home.set_brightness(Brightness.BRIGHT)
        self.smart_home.set_temperature(22)
        self.smart_home.set_is_security_armed(True)
        self.smart_home.set_streaming_service(Service.UNKNOWN)
