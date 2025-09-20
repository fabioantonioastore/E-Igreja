from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from . import BaseModel


class CommunityModel(BaseModel):
    __tablename__ = "community"

    name: Mapped[str] = mapped_column(String(200))
    id: Mapped[UUID] = mapped_column(primary_key=True, default_factory=uuid4)
