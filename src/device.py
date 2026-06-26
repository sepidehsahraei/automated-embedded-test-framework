class FakeSTM32Device:
    """
    This class simulates a simple STM32-based embedded device.
    It behaves like a real device that receives commands and sends responses.
    """

    def __init__(self):
        # This variable stores whether the simulated STM32 is connected or not.
        self.connected = False

        # This dictionary stores supported commands and their expected responses.
        self.command_responses = {
            "PING": "PONG",
            "GET_STATUS": "OK",
            "READ_TEMP": "25.4",
            "RESET": "RESET_DONE",
        }

    def connect(self):
        # This line changes the device state to connected.
        self.connected = True

        # This line returns a message that confirms the connection.
        return "STM32 device connected"

    def send_command(self, command):
        # This condition checks whether the device is connected before accepting commands.
        if not self.connected:
            return "ERROR: Device not connected"

        # This condition checks whether the command exists in the supported command list.
        if command in self.command_responses:
            return self.command_responses[command]

        # This line returns an error message for unknown commands.
        return "ERROR: Unknown command"