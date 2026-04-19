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