from uuid import UUID

import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid6 import uuid7

from .base import CreatedUpdatedAtMixin


class Post(CreatedUpdatedAtMixin):
    __tablename__ = "posts"
    __mapper_args__ = {"eager_defaults": True}

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7, server_default=sa.func.generate_uuid7())
    text: Mapped[str]
    image: Mapped[str | None]

    # relations
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(
        "User",
        foreign_keys=user_id,
        back_populates="users",
    )
