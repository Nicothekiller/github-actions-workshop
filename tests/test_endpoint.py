from fastapi.testclient import TestClient

from app.endpoint import app


client = TestClient(app)


def test_post_suma_endpoint() -> None:
    response = client.post("/suma", json={"a": 2, "b": 3})

    assert response.status_code == 200
    assert response.json() == {"a": 5}


def test_post_resta_endpoint() -> None:
    response = client.post("/resta", json={"a": 5, "b": 3})

    assert response.status_code == 200
    assert response.json() == {"a": 2}


def test_post_multiplicacion_endpoint() -> None:
    response = client.post("/multiplicacion", json={"a": 2, "b": 3})

    assert response.status_code == 200
    assert response.json() == {"a": 6}
