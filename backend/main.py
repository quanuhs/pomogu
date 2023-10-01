from typing import List

from fastapi import Depends, FastAPI

from backend.schemas.user import SchemaUserRead, SchemaUserCreate, SchemaUserUpdate
from backend.models import Therapy, Therapist, TherapistTag, TherapistMethod, User

from backend.database import create_db_and_tables, drop_db, engine, get_async_session
from backend.user_handler import auth_backend, current_active_user, fastapi_users
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.routes import methods_router, tags_router, sessions_router, therapist_router

app = FastAPI()

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/token", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(SchemaUserRead, SchemaUserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(SchemaUserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(SchemaUserRead, SchemaUserUpdate),
    prefix="/users",
    tags=["users"],
)

app.include_router(
    therapist_router
)

app.include_router(
    sessions_router
)

app.include_router(
    tags_router
)

app.include_router(
    methods_router
)


origins = [
    "http://94.198.216.30:8000",
    "https://pomogu.su",
    "http://pomogu.su"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup():
    # await drop_db()
    res = await create_db_and_tables()
