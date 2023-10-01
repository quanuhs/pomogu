import uuid
import datetime
from pydantic import BaseModel

from backend.schemas.therapist import SchemaTherapist


class SchemaSession(BaseModel):



    id: uuid.UUID | None
    therapist: SchemaTherapist | None
    
    connect_link: str | None
    starts_at: datetime.datetime | None
    ended_at: datetime.datetime | None
    status: str | None

    alone: bool | None = True
    young: bool | None = False
    adult: bool | None = True
    allow_cancel: bool | None = True

    class Config:
        orm_mode = True
