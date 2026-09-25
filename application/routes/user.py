
from fastapi import APIRouter,Depends
from typing import Annotated
from application.schemas.user import User_validation,Connexion_Validation
from application.database import db_dependency
from application.services.user import UserAuth
from fastapi.security import OAuth2PasswordRequestForm




user_router = APIRouter(prefix="/users",tags=["Authentification"])


@user_router.post("/inscription")
async def creer_user( body: User_validation, db: db_dependency):
    service = UserAuth(db)
    return await service.creer_utilisateur(body)


@user_router.post("/connexion")
async def connexion(form_data: Annotated[OAuth2PasswordRequestForm,Depends()] , db:db_dependency):
    service = UserAuth(db)
    Body= Connexion_Validation(email=form_data.username,password=form_data.password)
    return await service.connexion(Body)

