from pydantic import BaseModel,EmailStr
from pydantic import BaseModel, EmailStr, Field


class User_validation(BaseModel):
    nom: str
    prenom: str
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)


class Connexion_Validation(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)