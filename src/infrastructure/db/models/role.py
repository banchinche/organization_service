from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid6 import uuid7

from .base import CreatedUpdatedAtMixin


class Role(CreatedUpdatedAtMixin):
    __tablename__ = "roles"
    __mapper_args__ = {"eager_defaults": True}

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7, server_default=sa.func.generate_uuid7())
    name: Mapped[str] = mapped_column(unique=True)

    # relations
    users: Mapped[list["Users"]] = relationship(
        "User",
        back_populates="role", cascade="all, delete-orphan"
    )
