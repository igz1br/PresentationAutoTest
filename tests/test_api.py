import requests
from fastapi.testclient import TestClient
from app.app import app
import pytest

client = TestClient(app)

def test_api_black_box():
    result = requests.post(url="http://127.0.0.1:8000/release/", params={"chat_id":10})
    assert result.status_code == 200
    data = result.json()
    assert data == 0.01

def test_api_white_box():
    result = client.post(url="/release", params={"chat_id":110})
    assert result.status_code == 200
    data = result.json()
    assert data == 110**2

def test_api_white_box_fail():
    result = client.post(url="/release", params={"chat_id":"qwerty"})
    assert result.status_code == 422

test_data_id = []
for i in range (0,10):
    test_data_id.append(i)

@pytest.mark.parametrize("id", test_data_id)
def test_api_ques(id):
    result = client.get(url="/question", params={"ques_id":id})
    assert result.status_code == 200
    data = result.json()
    assert data["id"] == id


