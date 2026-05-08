import requests

def create_teacher(base_url, payload, headers):
    response = requests.post(
        f"{base_url}/api/teacher",
        json=payload,
        headers=headers
    )
    return response