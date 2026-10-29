import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_status():
    client = app.test_client()
    response = client.get("/status")
    assert response.status_code == 200

def test_add():
    client = app.test_client()
    response = client.get("/add/2/3")
    data = response.get_json()
    assert data["result"] == 5

def test_404_returns_json():
    client = app.test_client()
    response = client.get("/does-not-exist")
    assert response.status_code == 404
    assert response.is_json
    assert response.get_json() == {"error": "Not found", "status": 404}


def test_500_returns_json(monkeypatch):
    def boom():
        raise RuntimeError("boom")

    monkeypatch.setitem(app.view_functions, "status", boom)
    monkeypatch.setitem(app.config, "PROPAGATE_EXCEPTIONS", False)
    client = app.test_client()
    response = client.get("/status")
    assert response.status_code == 500
    assert response.is_json
    assert response.get_json() == {"error": "Internal server error", "status": 500}
