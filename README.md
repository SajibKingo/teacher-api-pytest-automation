# Teachers API Automation - Pytest

## Project Overview
This project contains an automated API testing framework for the Teachers module of the Student Management APIs. 

We have automated the Authentication flow, complete CRUD operations and comprehensive Negative test scenarios using Python and Pytest. The framework utilizes dynamic data generation, reusable helper functions and session-level fixtures to ensure clean, non-repetitive and highly efficient test execution.

## Tools Used
- **Python:** Core programming language.
- **Pytest:** Testing framework for writing and executing tests.
- **Requests:** HTTP library for making API calls.
- **Faker:** Library for generating dynamic, randomized test data.
- **Python-dotenv:** For managing environment variables securely.
- **Pytest-HTML & Allure:** For generating detailed test execution reports.

## Project Structure
The framework is designed with a clean, modular architecture:

1. `tests/`
   - Contains all the test modules (`test_auth.py`, `test_create_teacher.py`, etc.) grouped by functionality.
2. `utils/`
   - `config.py`: Manages environment variables and base URLs.
   - `helper_functions.py`: Contains reusable logic to prevent duplicate code across tests.
3. `conftest.py`
   - Houses global Pytest fixtures. It handles session-level authentication (logging in only once per test session) and dynamic payload generation.
4. `.env`
   - Stores sensitive credentials and configuration data (Excluded from Git).

## Test Cases
We have implemented and executed a comprehensive suite of 10 test scripts covering various scenarios:

### Authentication Tests
1. **`test_login_success`:** (Happy Path) Sends valid credentials to the `/login` endpoint, validates a `200 OK` status, and ensures the authentication token is successfully generated and extracted.
2. **`test_login_invalid_credentials`:** (Negative Path) Intentionally sends an incorrect password to validate the API's error handling mechanisms, expecting a `400` or `401` unauthorized status code.

### Create (POST) Tests
3. **`test_create_teacher_success`:** (Happy Path) Sends a dynamically generated valid payload to create a teacher. Validates the `201 Created` status and asserts that the API response matches the sent data.
4. **`test_create_teacher_missing_field`:** (Negative Path) Attempts to create a teacher while intentionally omitting a required field (e.g., "name"). Validates that the API rejects the request with a `400 Bad Request` error.

### Retrieve (GET) Tests
5. **`test_get_all_teachers_schema`:** Fetches the entire list of teachers. It validates the `200 OK` status and loops through the response to assert that all data types match the expected schema structure.
6. **`test_get_teacher_by_department_filter`:** Creates a teacher dynamically, then queries the API using the `?department=` query parameter. Validates that the returned list strictly contains teachers from that specific department.
7. **`test_get_teacher_by_id`:** Creates a teacher and immediately queries the API using the newly generated `teacherId`. Validates that the fetched details perfectly match the created data.
8. **`test_get_teacher_invalid_id`:** (Negative Path) Queries the API using a randomized, non-existent `teacherId`. Validates that the API correctly returns a `404 Not Found` status.

### Update (PUT) Test
9. **`test_update_teacher_designation`:** Modifies existing data by creating a teacher, sending a PUT request to update their designation and name, and then performing a subsequent GET request to verify the updates were successfully saved in the database.

### Delete (DELETE) Test
10. **`test_delete_teacher_flow`:** Validates the complete lifecycle. It creates a teacher, sends a DELETE request ensuring a `200` or `204` success status, and then explicitly verifies the deletion by attempting a GET request on that ID, expecting a `404 Not Found`.

## Setup Instructions
To set up the project on your local machine, follow these steps:
1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd <your-repository-folder>
2. Install Dependencies:
   ```bash
   pip install pytest requests faker python-dotenv pytest-html allure-pytest
3. Environment Variables Setup:
   ```bash
   BASE_URL = http://54.255.195.111:5171
   USERNAME = admin
   PASSWORD = password123

## Running the Tests
Execute the tests using the pytest command:
- Run all tests: `pytest`
- Run with verbose logs: `pytest -v`
- Run a specific file: `pytest tests/test_create_teacher.py`

## Generating Reports
This framework supports two types of detailed execution reports:

1. Allure Report (Interactive visual dashboard):
   ```bash
   pytest --alluredir=allure-results
   allure serve allure-results
   
###### Allure Report Output:
   
<img width="2852" height="1524" alt="Allure Report" src="https://github.com/user-attachments/assets/f35415f1-e875-4df2-a808-dc8cc4730487" />

2. HTML Report (Standalone file):
   ```bash
   pytest --html=report.html --self-contained-html
   (Open the generated report.html file in any web browser)
   
###### HTML Report Output:
<img width="2848" height="1526" alt="HTML Report" src="https://github.com/user-attachments/assets/e2a5af9f-fd89-4305-a5f0-ca3ef3ae2ac0" />
