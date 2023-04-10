from uuid import UUID

import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid6 import uuid7

from .base import CreatedUpdatedAtMixin


class Organization(CreatedUpdatedAtMixin):
    __tablename__ = "organizations"
    __mapper_args__ = {"eager_defaults": True}

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7, server_default=sa.func.generate_uuid7())
    name: Mapped[str] = mapped_column(unique=True)

    # relations
    founder_id: Mapped[UUID] = mapped_column(ForeignKey("users.id", use_alter=True))
    founder: Mapped["User"] = relationship(
        "User",
        back_populates="owned_organization",
        uselist=False,
    )
    users: Mapped[list["User"]] = relationship(
        "User",
        back_populates="organization", cascade="all, delete-orphan"
    )
