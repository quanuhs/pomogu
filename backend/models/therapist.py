import datetime
import decimal
import uuid
from typing import Any, Set, List

from backend.database import Base
from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.ext.hybrid import hybrid_method
from sqlalchemy.ext.hybrid import hybrid_property

from backend.models.user import User
from backend.models.therapist_tag import TherapistTag
from backend.models.therapist_method import TherapistMethod
from backend.models.therapy_session import Therapy


class Image(Base):
    __tablename__ = "image"
    
    id: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4, primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    url: Mapped[str] = mapped_column(nullable = False)

    therapist_id: Mapped[UUID] = mapped_column(ForeignKey("therapist.id"))
    therapist: Mapped["Therapist"] = relationship(uselist = False, back_populates="images")


class Therapist(Base):

    __tablename__ = "therapist"

    def __init__(self, user_id, description):
        self.user_id = user_id
        self.description = description


    id: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4, primary_key=True)
    description: Mapped[str] = mapped_column(nullable=False)
    tags: Mapped[List["TherapistTag"]] = relationship(secondary="therapies_tag_association", uselist=True, lazy="selectin")
    methods: Mapped[List["TherapistMethod"]] = relationship(secondary="therapies_method_association", uselist=True, lazy="selectin")

    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))
    user: Mapped[User] = relationship(uselist = False, back_populates="therapist", lazy="immediate")

    images: Mapped[Image] = relationship(uselist = True, back_populates="therapist")

    @hybrid_property
    def name(self) -> str:
        return self.user.name
    
    
    @hybrid_property
    def avatar_url(self) -> str:
        return self.user.avatar_url

    therapies: Mapped[List["Therapy"]] = relationship("Therapy", back_populates="therapist", uselist=True)

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return self.__str__()
