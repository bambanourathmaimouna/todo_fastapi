from application.database import db_dependency
from application.schemas.user import User_validation, Connexion_Validation
from application.model.models import User

from fastapi import HTTPException, status
from loguru import logger
from sqlalchemy import select
from passlib.context import CryptContext

from application.jwt import create_token
 
pwd_context = CryptContext(schemes=["argon2"],deprecated="auto")


class UserAuth:
    def __init__(self, db: db_dependency):
        self.db = db

    async def creer_utilisateur( self, Body_user: User_validation):
        # Vérifier si l'utilisateur existe
        result = await self.db.execute(select(User).where(User.email == Body_user.email))
        utilisateur_existe = result.scalar_one_or_none()
        if utilisateur_existe:
            raise HTTPException( status_code=status.HTTP_409_CONFLICT, detail="Utilisateur existe déjà !")
        # Vérifier la longueur du mot de passe
        if len(Body_user.password.encode("utf-8")) > 72:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Le mot de passe ne doit pas dépasser 72 octets.")
        # Hacher le mot de passe
        password_hash = pwd_context.hash(Body_user.password)
        new_user = User(nom=Body_user.nom, prenom=Body_user.prenom,email=Body_user.email, password=password_hash)
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        logger.info("Utilisateur créé avec succès")
        return new_user
    
    async def connexion( self, user: Connexion_Validation):
        result = await self.db.execute( select(User).where(User.email == user.email))
        user_db = result.scalar_one_or_none()
        if not user_db or not pwd_context.verify(
            user.password , 
            user_db.password
        ):
            raise HTTPException (
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="identifiant incorrecte"
            )
        access_token=create_token({"sub": str (user_db.id)})


        return {"access_token" : access_token}