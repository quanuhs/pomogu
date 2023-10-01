import uuid

from backend.database import Base
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, String
from sqlalchemy.orm import mapped_column, Mapped, validates, relationship
from sqlalchemy.ext.hybrid import hybrid_property

from datetime import date


class User(SQLAlchemyBaseUserTableUUID, Base):
    extend_existing = True

    name: Mapped[str] = mapped_column(nullable=False)
    birthday: Mapped[date] = mapped_column(nullable=False)
    therapist = relationship("Therapist", uselist = False, back_populates="user")
    avatar_url: Mapped[str] = mapped_column(nullable=False, default=f"https://api.dicebear.com/6.x/lorelei-neutral/svg?backgroundColor=transparent&seed={uuid.uuid4().hex}")

    def __str__(self):
        return self.name or self.email