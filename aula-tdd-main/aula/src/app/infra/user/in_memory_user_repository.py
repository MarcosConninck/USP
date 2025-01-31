from domain.user.user_repository_interface import UserRepositoryInterface
from domain.user.user_entity import User
from uuid import UUID


class InMemoryUserRepository(UserRepositoryInterface):

    def __init__(self):
        self.users: list[User] = []

    def save(self, user: User):
        self.users.append(user)

    def get_by_id(self, user_id: UUID):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def update_user_name(self, user_id: UUID, new_name):
        for user in self.users:
            if user.id == user_id:
                user.name = new_name
                return user
        # return None
