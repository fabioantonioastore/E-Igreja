from __future__ import annotations
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import BaseModel


if TYPE_CHECKING:
    from . import CommunityModel, LoginModel


class UserModel(BaseModel):
    __tablename__ = "user"

    name: Mapped[str] = mapped_column(String(200))
    cpf: Mapped[bytes | None] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(String(320), unique=True)
    phone_number: Mapped[str | None] = mapped_column(unique=True)
    community_id: Mapped[UUID | None] = mapped_column(ForeignKey("community.id", onupdate="CASCADE", ondelete="SET NULL"))

    community: Mapped[CommunityModel] = relationship()
    login: Mapped[LoginModel] = relationship()

    id: Mapped[UUID] = mapped_column(primary_key=True, default_factory=uuid4)
    role: Mapped[str] = mapped_column(String(100), default="faithful")
    rule: Mapped[str] = mapped_column(String(100), default="user")
    active: Mapped[bool] = mapped_column(default=True)
