from fastapi.testclient import TestClient
from uuid import UUID, uuid4
from infra.api.main import app

client = TestClient(app)

# testar se é possivel criar um usuário através da api


def test_can_create_user():

    response = client.post("/users/", json={"name": "José"})

    data = response.json()

    assert response.status_code == 200
    assert isinstance(UUID(data['id']), UUID)
    assert data['name'] == 'José'
