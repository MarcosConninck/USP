import pytest
from uuid import uuid4
from domain.user.user_entity import User


class TestUser():

    # Teste para o construtor do usuário
    def test_user_init(self):
        user_id = uuid4()
        user_name = "xandao"
        user = User(id=user_id, name=user_name)

        assert user.id == user_id, "user.id deve ser igual a user_id"
        assert user.name == user_name, "user.name deve ser igual ao user_name"

    # Teste para validar ID do usuário
    def test_user_id_validation(self):
        with pytest.raises(Exception, match="id must be an UUID"):
            User(id="id_invalido", name="Zé")

    # Teste para validar name do usuário
    def test_user_name_validation(self):
        user_id = uuid4()
        with pytest.raises(Exception, match="name is required"):
            User(id=user_id, name="")
