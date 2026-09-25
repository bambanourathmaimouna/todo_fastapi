from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import jwt
from typing import Annotated
from application.database import db_dependency
from application.model.models import User
from application.jwt import decode_token
from sqlalchemy import select
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/connexion")

SECRET_KEY = "ta-cle-secrete"
ALGORITHM = "HS256"


async def get_current_user(db: db_dependency,token: str = Depends(oauth2_scheme)) ->User:
    playload= decode_token(token)
    if playload is None :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED , 
            detail="Token invalide "
        )
    user_id=int(playload.get("sub"))
    resultat= await db.execute(select(User).where(User.id==user_id))
    user_curent =resultat.scalar_one_or_none()

    if not user_curent :
        raise HTTPException (
            status_code=status.HTTP_401_UNAUTHORIZED ,
            detail="utilisateur intravable "
        )


    return user_curent



current_user_dependency= Annotated[User , Depends(get_current_user)]









current_dependency = Annotated[ User,  Depends(get_current_user)]