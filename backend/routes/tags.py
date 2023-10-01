import datetime
import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete, select
from backend.database import AsyncSession, get_async_session
from backend.models import TherapistTag, User, Therapist
from backend.schemas.sessions import SchemaSession
from backend.user_handler import current_superuser, current_active_user


router = APIRouter(
    prefix="/tags",
    tags=["tags"],
)

@router.get("/")
async def all_tags(
    session: AsyncSession = Depends(get_async_session)
):
    results = await session.scalars(select(TherapistTag))
    return results.all()

@router.post("/")
async def create_tag(
    name: str,
    description: str = None,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user)
):
    if user.therapist is None:
        raise HTTPException(403)

    tag = TherapistTag(name=name, description=description)
    session.add(tag)
    await session.commit()

    return tag

@router.patch("/")
async def edit_tag(
    tag_id: uuid.UUID,
    name: str | None = None,
    description: str | None = None,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user)
):

    tag:TherapistTag = await session.scalar(select(TherapistTag).where(TherapistTag.id==tag_id))
    if tag is None:
        raise HTTPException(404)

    if name:
        tag.name = name
    
    if description:
        tag.description = description
    
    await session.commit()

    return tag



@router.delete("/")
async def delete_tag(
    tag_id: uuid.UUID,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_superuser)
):

    result = await session.scalar(select(TherapistTag).where(TherapistTag.id==tag_id))
    if result is None:
        raise HTTPException(404)

    await session.delete(result)
    await session.commit()

    return result


@router.post("/me")
async def asign_tag_me(
    tag_id: uuid.UUID,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user)
):
    therapist: Therapist | None = user.therapist

    if therapist is None:
        raise HTTPException(403)
     
    tag = await session.scalar(select(TherapistTag).where(TherapistTag.id==tag_id))

    if tag is None:
        raise HTTPException(404)

    therapist.tags.append(tag)

    await session.commit()
    return tag

@router.delete("/me")
async def remove_tag_me(
    tag_id: uuid.UUID,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user)
):
    therapist: Therapist | None = user.therapist

    if therapist is None:
        raise HTTPException(403)
     
    tag = await session.scalar(select(TherapistTag).where(TherapistTag.id==tag_id, Therapist.id == therapist.id, Therapist.tags.any(id = tag_id)))

    if tag is None:
        raise HTTPException(404)

    therapist.tags.remove(tag)

    await session.commit()
    return tag