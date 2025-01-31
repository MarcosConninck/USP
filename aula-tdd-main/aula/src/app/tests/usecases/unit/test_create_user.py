from unittest.mock import MagicMock
from uuid import UUID
from domain.user.user_repository_interface import UserRepositoryInterface
from application.user.create_user_use_case import \
    CreateUserUseCase, CreateUserRequest, CreateUserResponse


class TestCreateUser:

    # Teste para criar usuário com dados válidos

    def test_create_user_with_valid_data(self):

        # instanciar um repo (simulando os metodos que existem na interface)
        mock_repository = MagicMock(UserRepositoryInterface)

        # instanciar um caso de uso(com base no mock_repository)
        use_case = CreateUserUseCase(repository=mock_repository)

        # trazer input(request)
        request = CreateUserRequest(name='Marcos')

        # retornar um output(response)
        response = use_case.execute(request)

        assert response.id is not None
        assert isinstance(response, CreateUserResponse)
        assert isinstance(response.id, UUID)
        assert mock_repository.save.called is True
