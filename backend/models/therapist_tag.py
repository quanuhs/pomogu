import datetime
import decimal
import uuid
from typing import Set, List

from backend.database import Base
from sqlalchemy import Column, Integer, String, UUID, Table, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, mapped_column, Mapped, validates
from backend.models.user import User


class TherapistTag(Base):
    __tablename__ = "therapist_tag"


    def __init__(self, name:str, description:str = None):
        self.name = name
        self.description = description

    id: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4, primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    is_active: Mapped[bool] = mapped_column(nullable=False, default=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
