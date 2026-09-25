from application.database import Base
from sqlalchemy import Column,String,Integer,Boolean,DateTime ,ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime

class User(Base):

    __tablename__ = "users"
    
    id = Column(Integer,autoincrement=True,index=True,primary_key=True)
    nom = Column(String)
    prenom = Column(String)
    email = Column(String,unique=True,nullable=False)
    password = Column(String ,nullable= False)
    date_de_creation = Column(DateTime, default=datetime.now)



class Tasks(Base):

    __tablename__ = "tasks"
    
    id = Column(Integer,autoincrement=True,index=True,primary_key=True)
    titre = Column(String)
    description = Column(String)
    priorite = Column(String)
    completer = Column(Boolean,default=False)
    user_id = Column(Integer , ForeignKey("users.id"))
    date_de_creation = Column(DateTime, default=datetime.now)