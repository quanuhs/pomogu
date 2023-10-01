import datetime
import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete, select
from backend.database import AsyncSession, get_async_session
from backend.models import TherapistMethod, User, Therapist
from backend.schemas.sessions import SchemaSession
from backend.user_handler import current_superuser, current_active_user


router = APIRouter(
    prefix="/methods",
    tags=["methods"],
)

@router.get("/")
async def all_methods(
    session: AsyncSession = Depends(get_async_session)
):
    results = await session.scalars(select(TherapistMethod))
    return results.all()

@router.post("/")
async def create_method(
    name: str,
    description: str = None,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user)
):
    if user.therapist is None:
        raise HTTPException(403)

    method = TherapistMethod(name=name, description=description)
    session.add(method)
    await session.commit()

    return method

@router.patch("/")
async def edit_method(
    method_id: uuid.UUID,
    name: str | None = None,
    description: str | None = None,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user)
):

    method:TherapistMethod = await session.scalar(select(TherapistMethod).where(TherapistMethod.id==method_id))
    if method is None:
        raise HTTPException(404)

    if name:
        method.name = name
    
    if description:
        method.description = description
    
    await session.commit()

    return method


@router.delete("/")
async def delete_method(
    method_id: uuid.UUID,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_superuser)
):

    result = await session.scalar(select(TherapistMethod).where(TherapistMethod.id==method_id))
    if result is None:
        raise HTTPException(404)

    await session.delete(result)
    await session.commit()

    return result


@router.post("/me")
async def asign_method_me(
    method_id: uuid.UUID,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user)
):
    therapist: Therapist | None = user.therapist

    if therapist is None:
        raise HTTPException(403)
     
    method = await session.scalar(select(TherapistMethod).where(TherapistMethod.id==method_id))

    if method is None:
        raise HTTPException(404)

    therapist.methods.append(method)

    await session.commit()
    return method

@router.delete("/me")
async def remove_method_me(
    method_id: uuid.UUID,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user)
):
    therapist: Therapist | None = user.therapist

    if therapist is None:
        raise HTTPException(403)
     
    method = await session.scalar(select(TherapistMethod).where(TherapistMethod.id==method_id, Therapist.id == therapist.id, Therapist.methods.any(id = method_id)))

    if method is None:
        raise HTTPException(404)

    therapist.methods.remove(method)

    await session.commit()
    return method