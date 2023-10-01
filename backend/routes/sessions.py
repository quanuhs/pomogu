import datetime
import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete, select
from backend.database import AsyncSession, get_async_session
from backend.models import Therapy, User, Therapist
from backend.schemas.sessions import SchemaSession
from backend.user_handler import current_superuser, current_active_user


router = APIRouter(
    prefix="/sessions",
    tags=["sessions"],
)

@router.get("/", response_model=list[SchemaSession])
async def all_sessions(
    session: AsyncSession = Depends(get_async_session)
):
    therapy_session = await session.scalars(select(Therapy))
    
    # if therapy_session is None:
    #     raise HTTPException(404)

    # result:SchemaSession = SchemaSession.from_orm(therapy_session)
    # result.avatar_url = therapy_session.therapist.avatar_url

    return therapy_session.all()



@router.post("/join")
async def join_session(
    therapy_id: uuid.UUID,
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session)
):
    therapy_session: Therapy | None = await session.scalar(select(Therapy).join(Therapy.therapist).join(Therapist.user).where(
        Therapy.therapist != user).where(Therapy.id == therapy_id).where(therapy_session.status == "open"))
    
    if therapy_session is None:
        raise HTTPException(404)
   
    clients = therapy_session.clients
    clients.append(user)
    await session.commit()

    result:SchemaSession = SchemaSession.from_orm(therapy_session)

    return result



@router.get("/client/all", response_model=list[SchemaSession])
async def get_all_my_sessions_as_client(
    history: bool = False,
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session)
):
    _show_history = (Therapy.status == "busy")

    if history:
        _show_history = (Therapy.status != "busy")
    


    request = await session.scalars(select(Therapy).where(Therapy.clients.any(id = user.id)).where(_show_history).order_by(Therapy.starts_at))
    therapy_sessions = request.all()

    return therapy_sessions



@router.get("/therapist/all", response_model=list[SchemaSession])
async def get_all_my_sessions_as_therapist(
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session)
):
    request = await session.scalars(select(Therapy).join(Therapy.therapist).where(Therapist.user == user))
    therapy_sessions = request.all()

    return therapy_sessions


@router.post("/therapist/end", response_model=SchemaSession)
async def get_all_my_sessions_as_therapist(
    therapy_id: uuid.UUID,
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session)
):
    therapy_session: Therapy | None = await session.scalar(select(Therapy).join(Therapy.therapist).where(Therapist.user == user, Therapy.id==therapy_id, Therapy.status=="close", Therapy.ended_at == None))

    if therapy_session is None:
        raise HTTPException(404)
    
    _ends_at = datetime.datetime.now(therapy_session.starts_at.tzinfo)
    if therapy_session.starts_at < _ends_at:
        therapy_session.ended_at = _ends_at
        await session.commit()
    else:
        # Нельзя завершить до того как оно началось!
        raise HTTPException(400)
    
    return therapy_session




@router.post("/me/create")
async def create_session_me(
    start_date: datetime.datetime = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=3), name='МСК')),
    session:AsyncSession = Depends(get_async_session),
    user:User = Depends(current_active_user),
):
    therapist:Therapist | None = await session.scalar(select(Therapist).where(Therapist.user_id == user.id))

    if therapist is None:
        raise HTTPException(403)
    
    therapy_session = Therapy(starts_at=start_date, therapist_id=therapist.id)

    session.add(therapy_session)
    await session.commit()

    return therapy_session
