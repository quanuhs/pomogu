import uuid
from pydantic import BaseModel


class SchemaTag(BaseModel):
    id: uuid.UUID | None
    name: str | None
    description: str | None
    is_active: bool | None

    class Config:
        orm_mode = True

class SchemaMethod(BaseModel):
    id: uuid.UUID | None
    name: str | None
    description: str | None
    is_active: bool | None

    class Config:
        orm_mode = True

class SchemaTherapist(BaseModel):

    id: uuid.UUID | None
    name: str | None
    description: str | None
    price: int = 1800
    avatar_url: str | None

    tags: list[SchemaTag] = None
    methods: list[SchemaMethod] = None

    class Config:
        orm_mode = True


class SchemaTherapistAll(SchemaTherapist):
    user_id: uuid.UUID | None