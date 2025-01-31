from uuid import UUID
from application.user.create_user_use_case import \
    CreateUserUseCase, CreateUserRequest
from infra.user.in_memory_user_repository import InMemoryUserRepository


class TestCreateUser:

    # Teste para criar usuário com dados válidos

    def test_create_user_with_valid_data(self):

        # instanciar um repo (simulando os metodos que existem na interface)
        repository = InMemoryUserRepository()

        # instanciar um caso de uso(com base no repository)
        use_case = CreateUserUseCase(repository=repository)

        # trazer input(request)
        request = CreateUserRequest(name='Marcos')

        # retornar um output(response)
        response = use_case.execute(request)

        assert len(repository.users) == 1
        assert isinstance(response.id, UUID)

        persisted_user = repository.users[0]

        assert persisted_user.id == response.id
        assert persisted_user.name == 'Marcos'
