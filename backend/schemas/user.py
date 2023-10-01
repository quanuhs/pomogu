import uuid
from fastapi_users import schemas
from datetime import date

class SchemaUserRead(schemas.BaseUser[uuid.UUID]):
    name: str
    birthday: date
    avatar_url: str


class SchemaUserCreate(schemas.BaseUserCreate):
    name: str
    birthday: date
    

class SchemaUserUpdate(schemas.BaseUserUpdate):
    name: str
    birthday: date
    avatar_url: str
