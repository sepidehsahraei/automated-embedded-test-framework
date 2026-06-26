from src.logger import setup_logger
from src.device import FakeSTM32Device
from src.serial_interface import SerialInterface
from src.report_generator import TestReportGenerator


logger = setup_logger()

logger.info("Test framework started")

device = FakeSTM32Device()
serial = SerialInterface(device)

connection_result = serial.open()
logger.info(connection_result)

test_cases = [
    {"command": "PING", "expected_response": "PONG"},
    {"command": "GET_STATUS", "expected_response": "OK"},
    {"command": "READ_TEMP", "expected_response": "25.4"},
    {"command": "RESET", "expected_response": "RESET_DONE"},
    {
        "command": "INVALID_COMMAND",
        "expected_response": "ERROR: Unknown command",
    },
]

test_results = []

for test_case in test_cases:
    command = test_case["command"]
    expected_response = test_case["expected_response"]

    logger.info(f"Sending command: {command}")

    actual_response = serial.send(command)

    logger.info(f"Expected response: {expected_response}")
    logger.info(f"Received response: {actual_response}")

    if actual_response == expected_response:
        result = "PASS"
    else:
        result = "FAIL"

    logger.info(f"Test result: {result}")

    test_results.append(
        {
            "command": command,
            "expected_response": expected_response,
            "actual_response": actual_response,
            "result": result,
        }
    )

close_result = serial.close()
logger.info(close_result)

report_generator = TestReportGenerator()
report_file = report_generator.generate_csv_report(test_results)

logger.info(f"Test report generated: {report_file}")
logger.info("Test framework finished")