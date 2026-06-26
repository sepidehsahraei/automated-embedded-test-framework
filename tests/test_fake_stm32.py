import pytest

from src.device import FakeSTM32Device
from src.logger import setup_logger
from src.serial_interface import SerialInterface


logger = setup_logger()

@pytest.fixture
def connected_device():
    device = FakeSTM32Device()
    device.connect()
    return device


@pytest.fixture
def serial_interface():
    device = FakeSTM32Device()
    interface = SerialInterface(device)
    interface.open()
    return interface


def test_device_connection():
    device = FakeSTM32Device()

    response = device.connect()

    assert response == "STM32 device connected"
    assert device.connected is True


def test_command_without_connection():
    device = FakeSTM32Device()

    response = device.send_command("PING")

    assert response == "ERROR: Device not connected"


@pytest.mark.parametrize(
    "command, expected_response",
    [
        ("PING", "PONG"),
        ("GET_STATUS", "OK"),
        ("READ_TEMP", "25.4"),
        ("RESET", "RESET_DONE"),
        ("INVALID_COMMAND", "ERROR: Unknown command"),
    ],
)
def test_device_commands(connected_device, command, expected_response):
    logger.info(f"Starting test: {command} command")

    response = connected_device.send_command(command)

    logger.info(f"Expected response: {expected_response}")
    logger.info(f"Actual response: {response}")

    assert response == expected_response

    logger.info(f"Test result: PASS - {command} command")


def test_serial_interface_open():
    device = FakeSTM32Device()
    interface = SerialInterface(device)

    response = interface.open()

    assert response == "STM32 device connected"
    assert interface.is_open is True


def test_serial_interface_send_ping(serial_interface):
    response = serial_interface.send("PING")

    assert response == "PONG"


def test_serial_interface_send_invalid_command(serial_interface):
    response = serial_interface.send("INVALID_COMMAND")

    assert response == "ERROR: Unknown command"


def test_serial_interface_send_when_closed():
    device = FakeSTM32Device()
    interface = SerialInterface(device)

    response = interface.send("PING")

    assert response == "ERROR: Serial interface not open"


def test_serial_interface_close(serial_interface):
    response = serial_interface.close()

    assert response == "Serial interface closed"
    assert serial_interface.is_open is False