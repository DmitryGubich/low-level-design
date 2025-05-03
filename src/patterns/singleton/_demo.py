from patterns.singleton.printer_service import PrinterService

if __name__ == "__main__":
    worker1 = PrinterService()
    worker2 = PrinterService()

    worker1.set_mode("Color")
    worker2.set_mode("Grayscale")

    worker1_mode = worker1.get_printer_status()
    worker2_mode = worker2.get_printer_status()

    print(worker1_mode)
    print(worker2_mode)
