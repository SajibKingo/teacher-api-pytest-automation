import pytest
import requests
from utils.config import BASE_URL
from utils.helper_functions import create_teacher

def test_delete_teacher_flow(auth_headers, teacher_payload):
    post_response = create_teacher(BASE_URL, teacher_payload, auth_headers)
    created_id = post_response.json()["teacherId"]
    
    delete_response = requests.delete(f"{BASE_URL}/api/teacher/{created_id}", headers=auth_headers)
    assert delete_response.status_code in [200, 204], "Delete failed"
    
    get_response = requests.get(f"{BASE_URL}/api/teacher/{created_id}", headers=auth_headers)
    assert get_response.status_code == 404, "Deleted teacher still exists!"