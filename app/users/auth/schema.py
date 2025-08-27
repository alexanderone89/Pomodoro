from pydantic import BaseModel, Field


class GoogleUserData(BaseModel):
    id: int
    email: str
    name: str
    verified_email: bool
    access_token: str

class YandexUserData(BaseModel):
    id: int
    login: str
    default_email: str
    name: str = Field(alias='real_name')
    access_token: str

class UserLoginSchema(BaseModel):
    user_id: int
    access_token: str
