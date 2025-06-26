from typing import Annotated

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from starlette import status

from dependecy import get_auth_service
from exception import UserNotFoundException, UserNotCorrectPasswordException
from schema import UserLoginSchema, UserCreateSchema
from service.auth import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login",
             response_model=UserLoginSchema)
async def login(body: UserCreateSchema,
                auth_service: Annotated[AuthService,Depends(get_auth_service)]):
    try:
        return auth_service.login(body.username, body.password)
    except UserNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e.detail)
    except UserNotCorrectPasswordException as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=e.detail)
