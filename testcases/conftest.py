import pytest
import requests
from faker import Faker
from utils.config import BASE_URL, USERNAME, PASSWORD

@pytest.fixture()
def login_data():
    return {
        "username": USERNAME,
        "password": PASSWORD
    }

@pytest.fixture()
def auth_headers(login_data):
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    token = response.json().get("authToken")
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

@pytest.fixture
def teacher_schema():
    return {
        "teacherId": int,
        "name": str,
        "email": str,
        "department": str,
        "designation": str
    }

fake = Faker()

@pytest.fixture
def teacher_payload():
    return{
        "name": fake.name(),
        "email": fake.email(),
        "department": "CSE",
        "teacherId": fake.random_int(min=10000, max=99999),
        "designation": fake.random_element(elements=("Professor", "Lecturer", "Assistant Professor"))
    }
