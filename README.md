# Automated Embedded Test Framework

A Python-based test automation framework for validating embedded device behavior.

The project simulates an embedded device interface and uses `pytest` to automatically verify device commands, responses, error handling, and connection behavior.
Real UART-based hardware validation is implemented separately in the FRDM-MCXA153 hardware test project.

## Features

- Automated test execution with `pytest`
- Simulated embedded device interface
- Command-response validation
- Connection and error handling tests
- Logging and test reporting
- JUnit XML test report generation
- Jenkins CI pipeline
- Automatic build triggering through SCM polling

## Technologies

- Python
- pytest
- Git / GitHub
- Jenkins
- JUnit XML
- Logging

## Project Structure

```text
automated-embedded-test-framework/
├── src/
│   ├── device.py
│   ├── logger.py
│   ├── serial_interface.py
│   └── report_generator.py
├── tests/
│   └── test_fake_stm32.py
├── Jenkinsfile
├── requirements.txt
├── main.py
└── README.md
```

## Automated Tests

The test suite validates several device behaviors, including:

- Device connection
- Command execution
- Status requests
- Temperature reading
- Device reset
- Invalid commands
- Commands sent while disconnected

Run the tests locally with:

```bash
python -m pytest
```

## Jenkins CI Pipeline

The repository includes a Jenkins pipeline defined in the `Jenkinsfile`.

The pipeline automatically:

1. Checks out the latest source code from GitHub.
2. Installs Python dependencies from `requirements.txt`.
3. Runs the automated test suite with `pytest`.
4. Generates a JUnit XML test report.
5. Publishes the test results in Jenkins.

### CI Workflow

```text
Git push
   ↓
Jenkins detects repository changes
   ↓
Checkout source code
   ↓
Install dependencies
   ↓
Run pytest
   ↓
Generate JUnit XML report
   ↓
Publish test results
```

## Current Test Result

```text
12 tests passed
```

## Future Improvements

- Integration with the separate FRDM-MCXA153 hardware test project for real serial hardware validation.
- Hardware-in-the-loop testing
- Additional GPIO, UART, ADC, PWM, I2C, and SPI test cases
- Extended CI automation
