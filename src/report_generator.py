import csv
from pathlib import Path


REPORT_DIR = Path("reports")
REPORT_FILE = REPORT_DIR / "test_report.csv"


class TestReportGenerator:
    """
    This class creates a CSV report for executed test commands.
    Each row contains the command, expected response, actual response, and test result.
    """

    def __init__(self):
        REPORT_DIR.mkdir(exist_ok=True)

    def generate_csv_report(self, test_results):
        with open(REPORT_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(
                ["Command", "Expected Response", "Actual Response", "Result"]
            )

            for result in test_results:
                writer.writerow(
                    [
                        result["command"],
                        result["expected_response"],
                        result["actual_response"],
                        result["result"],
                    ]
                )

        return REPORT_FILE