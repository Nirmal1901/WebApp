import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.main import app, calculate_discount


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json["status"] == "ok"


def test_get_users(client):
    res = client.get("/users")
    assert res.status_code == 200
    assert "users" in res.json
    assert len(res.json["users"]) >= 2


def test_get_user(client):
    res = client.get("/users/1")
    assert res.status_code == 200
    assert res.json["name"] == "Alice"


def test_get_user_not_found(client):
    res = client.get("/users/999")
    assert res.status_code == 404


def test_create_user(client):
    res = client.post(
        "/users",
        json={"name": "Charlie", "email": "charlie@example.com"},
    )
    assert res.status_code == 201
    assert res.json["name"] == "Charlie"


def test_create_user_missing_fields(client):
    res = client.post("/users", json={"name": "NoEmail"})
    assert res.status_code == 400


def test_delete_user(client):
    res = client.delete("/users/2")
    assert res.status_code == 200
    assert res.json["deleted"]["name"] == "Bob"


def test_calculate_discount():
    assert calculate_discount(100, 10) == 90.0
    assert calculate_discount(200, 50) == 100.0
    assert calculate_discount(100, 0) == 100.0


def test_calculate_discount_invalid():
    with pytest.raises(ValueError):
        calculate_discount(100, -5)
    with pytest.raises(ValueError):
        calculate_discount(100, 110)
