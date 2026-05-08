import pytest
import requests
from utils.config import BASE_URL

def test_login_success(login_data):
    response = requests.post(f"{BASE_URL}/login", json=login_data)

    assert response.status_code == 200, f"Login failed. Response: {response}" 

    token = response.json().get("authToken")

    assert token is not None, "Auth token not found in response"


def test_login_invalid_credentials():
    payload = {"username": "admin", "password": "wrongpassword"}
    response = requests.post(f"{BASE_URL}/login", json=payload)

    assert response.status_code in [400, 401], f"Expected auth error, got {response.status_code}"