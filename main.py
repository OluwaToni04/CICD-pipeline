from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data
    assert data["status"] == "running"


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_version():
    client = app.test_client()
    response = client.get("/version")
    assert response.status_code == 200
    data = response.get_json()
    assert "version" in data


def test_info():
    client = app.test_client()
    response = client.get("/info")
    assert response.status_code == 200
    data = response.get_json()
    assert data["developer"] == "Oluwatoni Ajaka"