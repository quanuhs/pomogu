import datetime
import decimal
import uuid
from typing import Set, List

from backend.database import Base
from sqlalchemy import Column, Integer, String, UUID, Table, ForeignKey, DateTime, func, case
from sqlalchemy.orm import relationship, mapped_column, Mapped, validates
from backend.models.user import User
from sqlalchemy.ext.hybrid import hybrid_property



class Therapy(Base):
    __tablename__ = "therapy"

    def __init__(self, starts_at: datetime.datetime, therapist_id:uuid.UUID):
        self.therapist_id = therapist_id
        self.starts_at = starts_at

    id: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4, primary_key=True)

    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), nullable=False)
    starts_at: Mapped[datetime.datetime] = mapped_column(nullable=False)
    ended_at: Mapped[datetime.datetime] = mapped_column(nullable=True)
    canceled_at: Mapped[datetime.datetime] = mapped_column(nullable=True)

    clients: Mapped[List[User]] = relationship(uselist=True, backref="therapies",
                                               secondary="therapies_association", lazy="immediate")

    therapist_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("therapist.id"))
    therapist = relationship('Therapist', back_populates="therapies", lazy="immediate")


    @hybrid_property
    def status(self) -> str:
        res = "open"
        
        if self.clients:
            res = "busy"

        if self.ended_at is not None:
            res = "ended"

        elif self.starts_at <= datetime.datetime.now(self.starts_at.tzinfo):
            res = "ended"
        
        return res
    
    @status.expression
    def status(cls) -> str:
        return case(
            (cls.ended_at.isnot(None), "ended"),
            (cls.starts_at <= datetime.datetime.now(), "ended"),
            else_=case((cls.clients != None, "busy"), else_="open")
        )


    @hybrid_property
    def avatar_url(self) -> str:
        return self.therapist.avatar_url


    def calculate_duration(self):
        return self.ended_at - self.starts_at

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return self.__str__()
