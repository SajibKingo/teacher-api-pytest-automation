import pytest
import requests
from utils.config import BASE_URL
from utils.helper_functions import create_teacher

def test_update_teacher_designation(auth_headers, teacher_payload):
    post_response = create_teacher(BASE_URL, teacher_payload, auth_headers)
    created_id = post_response.json()["teacherId"]
    
    updated_payload = {
        "name": teacher_payload["name"] + " Updated",
        "designation": "Head of Department"
    }
    
    put_response = requests.put(
        f"{BASE_URL}/api/teacher/{created_id}",
        json=updated_payload,
        headers=auth_headers
    )
    assert put_response.status_code in [200, 201], "Update failed"
    
    get_response = requests.get(f"{BASE_URL}/api/teacher/{created_id}", headers=auth_headers)
    assert get_response.json()["designation"] == "Head of Department"