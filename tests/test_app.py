from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# Test without authentication

def test_root_unauthorized():
    r = client.get("/")
    assert r.status_code == 401


def test_health_unauthorized():
    r = client.get("/health")
    assert r.status_code == 401

# Test authentication

def test_login():
    r = client.post("/token", data={"username": "testuser", "password": "fakehashedsecret"})
    assert r.status_code == 200
    assert "access_token" in r.json()


def test_root_authorized():
    login_response = client.post("/token", data={"username": "testuser", "password": "fakehashedsecret"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    r = client.get("/", headers=headers)
    assert r.status_code == 200
    assert r.json()["message"] == "hello"


def test_health_authorized():
    login_response = client.post("/token", data={"username": "testuser", "password": "fakehashedsecret"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    r = client.get("/health", headers=headers)
    assert r.status_code == 200
    assert r.json() == {"ok": True}