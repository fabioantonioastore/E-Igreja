from __future__ import annotations
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from . import BaseModel


if TYPE_CHECKING:
    from . import UserModel


class LoginModel(BaseModel):
    __tablename__ = "login"

    user_id: Mapped[UserModel] = mapped_column(ForeignKey("user.id", onupdate="CASCADE", ondelete="CASCADE"), unique=True)
    password: Mapped[bytes]
    id: Mapped[UUID] = mapped_column(primary_key=True, default_factory=uuid4)