from dataclasses import dataclass

from app.users.user_profile.repository import UserRepository
from app.users.auth.schema import UserLoginSchema
from app.users.user_profile.schema import UserCreateSchema
from app.users.auth.service import AuthService


@dataclass
class UserService:
    user_repository: UserRepository
    auth_service: AuthService

    # async def create_user(self, username: str, password: str)->UserLoginSchema:
    async def create_user(self, new_user: UserCreateSchema) -> UserLoginSchema:

        # user = await self.user_repository.create_user(username, password)
        # access_token = self.auth_service.generate_access_token(user_id=user.id)
        # return UserLoginSchema(user_id=user.id, access_token=access_token)
        user = await self.user_repository.create_user(new_user)
        access_token = self.auth_service.generate_access_token(user_id=user.id)
        return UserLoginSchema(user_id=user.id, access_token=access_token)

    # @staticmethod
    # def _generate_access_token(user_id: int)->str:
    #     return ''.join(choice(string.ascii_uppercase + string.digits)for _ in range(10))
