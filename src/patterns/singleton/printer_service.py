import threading


class PrinterService:
    _instance_lock = threading.Lock()
    _unique_instance = None

    def __new__(cls):
        with cls._instance_lock:
            if cls._unique_instance is None:
                cls._unique_instance = super().__new__(cls)
                cls._unique_instance._init_printer_service()

        return cls._unique_instance

    def _init_printer_service(self):
        self.mode = "GrayScale"

    def get_printer_status(self):
        return self.mode

    def set_mode(self, mode):
        self.mode = mode
        print(f"Mode changed to {mode}")
