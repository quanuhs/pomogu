from backend.database import Base
from sqlalchemy import Column, Table, ForeignKey

therapies_association_table = Table(
    "therapies_association",
    Base.metadata,
    Column("client_id", ForeignKey("user.id"), primary_key=True),
    Column("therapy_id", ForeignKey("therapy.id"), primary_key=True),
)

therapies_tag_association_table = Table(
    "therapies_tag_association",
    Base.metadata,
    Column("therapist_id", ForeignKey("therapist.id"), primary_key=True),
    Column("tag_id", ForeignKey("therapist_tag.id"), primary_key=True),
)

therapies_method_association_table = Table(
    "therapies_method_association",
    Base.metadata,
    Column("therapist_id", ForeignKey("therapist.id"), primary_key=True),
    Column("method_id", ForeignKey("therapist_method.id"), primary_key=True),
)
