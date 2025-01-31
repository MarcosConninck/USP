from domain.user.user_entity import User
from uuid import uuid4
from infra.user.in_memory_user_repository import InMemoryUserRepository
# salvar, retornar por id, atualiza, deleta, listar

# Test de save user


class TestSaveUser:

    def test_can_save_user(self):

        repository = InMemoryUserRepository()

        user1 = User(id=uuid4(), name='user1')
        user2 = User(id=uuid4(), name='user2')

        # salva usuario 1
        repository.save(user1)

        # salva usuario 2
        repository.save(user2)

        # verificar se os usuários estão no repositório
        # e se a lista de usuários tem 2 usuários

        assert len(repository.users) == 2
        assert repository.users[0] == user1
        assert repository.users[1] == user2


class TestGetUserById:
    # Testar se é possivel retornar um usuário pelo ID dele

    def test_can_get_user_by_id(self):

        repository = InMemoryUserRepository()

        user1 = User(id=uuid4(), name='user1')
        user2 = User(id=uuid4(), name='user2')

        repository.save(user1)
        repository.save(user2)

        # Retornar o usuário 1 pelo seu id
        user = repository.get_by_id(user1.id)

        # verifico se eu retorno o mesmo usuário
        assert user.id == user1.id
        assert user.name == user1.name

    # Testar se o método get_by_id retorna um obj vazio
    # caso não exista o user no rep
    def test_when_user_not_exists_should_return_none(self):

        repository = InMemoryUserRepository()

        user1 = User(id=uuid4(), name='user1')
        user2 = User(id=uuid4(), name='user2')

        repository.save(user1)
        repository.save(user2)

        user = repository.get_by_id(user_id=uuid4())

        assert user is None


class TestUpdateUser:

    # Testar se é possivel atualizar um nome do usuário
    def test_update_user_name(self):

        repository = InMemoryUserRepository()

        user1 = User(id=uuid4(), name='user1')
        user2 = User(id=uuid4(), name='user2')

        repository.save(user1)
        repository.save(user2)

        # Atualizando user1.name = 'marco'
        user = repository.update_user_name(user_id=user1.id, new_name='marco')

        assert user.name != 'user1'
