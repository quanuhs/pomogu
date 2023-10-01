import contextlib
import datetime
from functools import wraps
import uuid
from typing import Optional

from fastapi_users.authentication import CookieTransport
from fastapi import Depends, Request, Response
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users.authentication import (
    AuthenticationBackend,
)
from fastapi_users.authentication.strategy import DatabaseStrategy, AccessTokenDatabase
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.exceptions import UserAlreadyExists, UserNotExists
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTableUUID, SQLAlchemyAccessTokenDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_async_session, Base
from backend.models import User

from sqlalchemy import delete
from sqlalchemy.orm import mapped_column, Mapped

SECRET = "SECRET"


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_login(
            self, user: User, request: Optional[Request] = None,
            response: Optional[Response] = None) -> None:

        print(f"User {user.id} has logged in!")

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
            self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
            self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


class AccessToken(SQLAlchemyBaseAccessTokenTableUUID, Base):
    expires: Mapped[datetime.datetime] = mapped_column(default=(datetime.datetime.now() + datetime.timedelta(seconds=3600)))


async def get_access_token_db(session: AsyncSession = Depends(get_async_session), ):
    # await session.execute(delete(AccessToken).where(AccessToken.expires <= datetime.datetime.now()))
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


def get_auth_strategy(
        access_token_db: AccessTokenDatabase[AccessToken] = Depends(get_access_token_db), ) -> DatabaseStrategy:
    return DatabaseStrategy(access_token_db, lifetime_seconds=3600)


get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)

cookie_transport = CookieTransport(cookie_max_age=3600, cookie_secure=True, cookie_name="pomogu_auth",
                                   cookie_samesite="lax", cookie_domain="pomogu.su")

auth_backend = AuthenticationBackend(
    name="database",
    transport=cookie_transport,
    get_strategy=get_auth_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(superuser=True)
