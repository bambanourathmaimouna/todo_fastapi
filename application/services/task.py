from sqlalchemy.orm import Session
from sqlalchemy import select
from application.model.models import Tasks
from application.schemas.task import Task_validation
from application.database import db_dependency
from loguru import logger
from fastapi import  HTTPException

class Service_tache:
    def __init__(self, db:db_dependency):
        self.db = db

    async def creer_tache(self,task:Task_validation,current_id:int):
        nouvelle_tache = Tasks(
            titre = task.titre,
            description = task.description,
            priorite = task.priorite,
            completer = task.completer,
            user_id= current_id
        )

        self.db.add(nouvelle_tache)
        await self.db.commit()
        await self.db.refresh(nouvelle_tache)
        logger.info("tache crée avec succès ! ")

        return nouvelle_tache


    async def get_Taches(self, User_id: int):
        resultat = await self.db.execute(select(Tasks).where( Tasks.user_id == User_id ))
        task = resultat.scalars().all()
        if not task :
            raise HTTPException( status_code=404 , detail="depot vide ")
        return task


    async def modifier_tache(self, task_id: int, task: Task_validation, user_id: int):
        resultat = await self.db.execute(select(Tasks).where( Tasks.id == task_id,Tasks.user_id == user_id))
        tache = resultat.scalar_one_or_none()
        if tache is None:
            raise HTTPException( status_code=404,detail="Tâche introuvable")
        tache.titre = task.titre
        tache.description = task.description
        tache.priorite = task.priorite
        await self.db.commit()
        await self.db.refresh(tache)
        return tache


    async def supprimer_tache(self,task_id: int,user_id: int):
        resultat = await self.db.execute(select(Tasks).where( Tasks.id == task_id, Tasks.user_id == user_id ))
        tache = resultat.scalar_one_or_none()
        if tache is None:raise HTTPException(status_code=404, detail="Tâche introuvable")

        await self.db.delete(tache)
        await self.db.commit()
        return { "message": "Tâche supprimée avec succès"}
    

    async def filtrer_tache(self , User_id : int , tache_id :bool):
        resultat  = await self.db.execute(select(Tasks).where(Tasks.user_id== User_id , Tasks.completer==tache_id))
        tache= resultat.scalars().all()
        if not tache :
            raise HTTPException(status_code=404 , detail="pas de tache actife")

        return  tache


    async def filtrer_tache_id(self , User_id : int , tache_id :int):
            resultat  = await self.db.execute(select(Tasks).where(Tasks.user_id== User_id , Tasks.id==tache_id))
            tache= resultat.scalars().all()
            if not tache :
                raise HTTPException(status_code=404 , detail="pas de tache actife")
    
            return  tache
    
    async def filtrer_tache_titre(self , User_id : int , tache_id :str):
                resultat  = await self.db.execute(select(Tasks).where(Tasks.user_id== User_id , Tasks.titre==tache_id))
                tache= resultat.scalars().all()
                if not tache :
                    raise HTTPException(status_code=404 , detail="pas de tache actife")
        
                return  tache
        



