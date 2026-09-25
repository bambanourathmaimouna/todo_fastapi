from fastapi import APIRouter , Path
from application.schemas.task import Task_validation
from application.schemas.dependance import current_user_dependency
from application.database import db_dependency
from application.model.models import Tasks
from application.services.task import Service_tache
task_router = APIRouter(prefix= "/task",tags=["Tasks"])

@task_router.post("/create")
async def creer_tache(task:Task_validation,db:db_dependency,current_user:current_user_dependency):
    tache = Service_tache(db)
    return await tache.creer_tache(task, current_user.id)



@task_router.get("/")
async def get_taches(db: db_dependency,current_user: current_user_dependency):
    tache = Service_tache(db)
    return await tache.get_Taches(current_user.id)



@task_router.get("/filtrer_tache/{status}")
async def filtrer_Tache(  db: db_dependency, current_user: current_user_dependency , status:bool=Path() ):
    tache = Service_tache(db)
    return await tache.filtrer_tache(current_user.id ,status ) 

@task_router.get("/filtrer_tache_id/{id}")
async def filtrer_Tache_id(  db: db_dependency, current_user: current_user_dependency , id:int=Path() ):
    tache = Service_tache(db)
    return await tache.filtrer_tache_id(current_user.id ,id ) 

@task_router.get("/filtrer_tache_titre/{titre}")
async def filtrer_Tache_titre(  db: db_dependency, current_user: current_user_dependency , titre:str=Path() ):
    tache = Service_tache(db)
    return await tache.filtrer_tache_titre(current_user.id ,titre ) 

@task_router.put("/{task_id}")
async def modifier_tache(task_id: int, task: Task_validation,db: db_dependency, current_user: current_user_dependency):
    tache = Service_tache(db)
    return await tache.modifier_tache( task_id, task,current_user.id)


@task_router.delete("/{task_id}")
async def supprimer_tache(task_id: int, db: db_dependency, current_user: current_user_dependency):
    tache = Service_tache(db)
    return await tache.supprimer_tache(task_id,current_user.id)
