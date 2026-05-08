import pytest
import requests
from utils.config import BASE_URL
from utils.helper_functions import create_teacher

def test_get_all_teachers_schema(auth_headers, teacher_schema):
    response = requests.get(f"{BASE_URL}/api/teacher", headers=auth_headers)
    assert response.status_code == 200, "GET request failed"
    
    teachers = response.json()
    assert len(teachers) > 0, "No teachers found"
    
    for teacher in teachers:
        for key, expected_type in teacher_schema.items():
            if key in teacher: 
                assert isinstance(teacher[key], expected_type), \
                    f"Key '{key}' expected {expected_type}, got {type(teacher[key])}"
                


def test_get_teacher_by_department_filter(auth_headers, teacher_payload):
    create_teacher(BASE_URL, teacher_payload, auth_headers)
    dept_to_search = teacher_payload["department"]
    
    response = requests.get(f"{BASE_URL}/api/teacher?department={dept_to_search}", headers=auth_headers)
    assert response.status_code == 200
    
    teachers = response.json()
    for teacher in teachers:
        assert teacher["department"] == dept_to_search, "Filter returned incorrect department"



def test_get_teacher_by_id(auth_headers, teacher_payload):
    post_response = create_teacher(BASE_URL, teacher_payload, auth_headers)
    created_id = post_response.json()["teacherId"]
    
    response = requests.get(f"{BASE_URL}/api/teacher/{created_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["teacherId"] == created_id
    assert response.json()["email"] == teacher_payload["email"]



def test_get_teacher_invalid_id(auth_headers):
    invalid_id = 99999999
    response = requests.get(f"{BASE_URL}/api/teacher/{invalid_id}", headers=auth_headers)
    assert response.status_code == 404, "Expected 404 for non-existent ID"