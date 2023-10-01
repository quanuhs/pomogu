import datetime
from typing import Any, Dict, Optional
import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete, select
from sqlalchemy.orm import joinedload
from backend.database import AsyncSession, get_async_session
from backend.models import Therapist, User, Therapy
from backend.schemas.therapist import SchemaTherapist
from backend.user_handler import current_superuser, current_active_user



router = APIRouter(
    prefix="/therapist",
    tags=["therapists"],
)


class THERAPIST:
    class ALREADY_EXISTS(HTTPException):
        def __init__(self):
            pass

        status_code=406
        detail="Therapist already exists for this user"
        
        @classmethod
        def dict(cls):
            return {cls.status_code: {"description": cls.detail}}
    
    class NOT_FOUND(HTTPException):
        def __init__(self):
            pass

        status_code=404
        detail="Therapist not found"

        @classmethod
        def dict(cls):
            return {cls.status_code: {"description": cls.detail}}

    


# 
#   Для пользователя - терапевта
# 

# Создать терапевта
@router.post("/me",
    responses={**THERAPIST.ALREADY_EXISTS.dict()}
)
async def create_therapist_me(
    description:str,
    user:User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session)):

    result = await _create_therapist(session, user.id, description)
    return result


# Получить терапевта
@router.get("/me", 
    response_model=SchemaTherapist,
    responses={**THERAPIST.NOT_FOUND.dict()}
)
async def get_therapist_me(
    user:User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session)
):

    result = await _get_therapist(session, user_id=user.id)

    return SchemaTherapist.from_orm(result)


# Создать терапевта
@router.patch("/me",
    responses={**THERAPIST.NOT_FOUND.dict()}
)
async def edit_therapist_me(
    description:str,
    user:User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session)):

    result = await _create_therapist(session, user.id, description)
    return result


# Удалить терапевта
@router.delete("/me",
    responses={**THERAPIST.NOT_FOUND.dict()}
)
async def delete_therapist_me(
    user:User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session)):

    result = await _delete_therapist(session, user_id=user.id)

    return result



# 
#   Для всех пользователей
# 

# Получить всех терапевтов + фильтр
@router.get("/all",
            response_model=list[SchemaTherapist])
async def get_all_therapists(
    name: str = None,
    date: datetime.datetime = None,
    session: AsyncSession = Depends(get_async_session)):
    
    results = await session.scalars(select(Therapist).join(Therapy).where(Therapy.status=="close").group_by(Therapist.id))

    return results.all()


# Получить терапевта по id
@router.get("/{id}", 
    response_model=SchemaTherapist,
    responses={**THERAPIST.NOT_FOUND.dict()}
)
async def get_therapist(
    id: uuid.UUID,
    session: AsyncSession = Depends(get_async_session)
):
    result = await _get_therapist(session, id)
    return SchemaTherapist.from_orm(result)




# 
#   Для администратора
#

# Создать терапевта по id пользователя
@router.post("/", 
    responses={**THERAPIST.ALREADY_EXISTS.dict()},
    dependencies=[Depends(current_superuser)]
)
async def create_therapist(
    user_id: uuid.UUID,
    description: str,
    session: AsyncSession = Depends(get_async_session)
):
    therapist = await _create_therapist(session, user_id, description)
    return SchemaTherapist.from_orm(therapist)


# Удалить терапевта по id
@router.delete("/{id}",
    responses={**THERAPIST.ALREADY_EXISTS.dict()},
    response_model=SchemaTherapist,
    dependencies=[Depends(current_superuser)]
)
async def delete_therapist(
    id: uuid.UUID,
    session: AsyncSession = Depends(get_async_session)
):

    result = await _delete_therapist(session, therapist_id=id)
    return SchemaTherapist.from_orm(result)


#
# Для работы c API
#

async def _create_therapist(session:AsyncSession, user_id:uuid.UUID, description:str):
    result = await session.scalar(select(Therapist).where(Therapist.user_id==user_id))

    if result is not None:
        raise THERAPIST.ALREADY_EXISTS

    therapist = Therapist(user_id=user_id, description=description)

    session.add(therapist)
    await session.commit()

    return "CREATED"
    

async def _get_therapist(session:AsyncSession, therapist_id:uuid.UUID = None, user_id:uuid.UUID = None):
    result = None

    if therapist_id:
        result  = await session.scalar(select(Therapist).where(Therapist.id == therapist_id))
    elif user_id:
        result  = await session.scalar(select(Therapist).where(Therapist.user_id == user_id))

    if result is None:
        raise THERAPIST.NOT_FOUND
    
    return result


async def _delete_therapist(session:AsyncSession, therapist_id:uuid.UUID = None, user_id:uuid.UUID = None):
    result:Therapist = await _get_therapist(session, therapist_id, user_id)

    await session.delete(result)
    await session.commit()
    
    return {"Deleted"}