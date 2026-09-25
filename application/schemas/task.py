from pydantic import BaseModel

class Task_validation (BaseModel):
    titre:str
    description:str
    priorite:str
    completer:bool=False
    