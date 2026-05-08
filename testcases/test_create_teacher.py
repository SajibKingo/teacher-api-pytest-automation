import pytest
import requests
from utils.config import BASE_URL
from utils.helper_functions import create_teacher

def test_create_teacher_success(auth_headers, teacher_payload):
    response = create_teacher(BASE_URL, teacher_payload, auth_headers)

    print("Response:", response)

    assert response.status_code in [200, 201], f"Creation failed: {response}"
    
    data = response.json()

    assert data["name"] == teacher_payload["name"]
    assert data["email"] == teacher_payload["email"]
    assert data["teacherId"] == teacher_payload["teacherId"]



def test_create_teacher_missing_field(auth_headers, teacher_payload):
    del teacher_payload["name"] 
    response = create_teacher(BASE_URL, teacher_payload, auth_headers)

    assert response.status_code == 400, "API should reject payload with missing required fields"