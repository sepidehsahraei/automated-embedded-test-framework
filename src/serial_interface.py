class SerialInterface:
    """
    This class represents the communication interface between
    the test framework and the embedded device.

    In this version, it communicates with a fake STM32 device.
    Later, it can be extended to communicate with a real STM32
    through a serial port.
    """

    def __init__(self, device):
        self.device = device
        self.is_open = False

    def open(self):
        response = self.device.connect()
        self.is_open = True
        return response

    def close(self):
        self.is_open = False
        return "Serial interface closed"

    def send(self, command):
        if not self.is_open:
            return "ERROR: Serial interface not open"

        return self.device.send_command(command)