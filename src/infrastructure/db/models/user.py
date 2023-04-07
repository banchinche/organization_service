from uuid import UUID

import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid6 import uuid7

from .base import CreatedUpdatedAtMixin


class User(CreatedUpdatedAtMixin):
    __tablename__ = "users"
    __mapper_args__ = {"eager_defaults": True}

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7, server_default=sa.func.generate_uuid7())
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str]

    # relations
    organization_id: Mapped[UUID] = mapped_column(ForeignKey("organizations.id"), nullable=True)
    organization: Mapped["Organization"] = relationship(
        "Organization",
        foreign_keys=organization_id,
        back_populates="users",
    )
    owned_organization: Mapped["Organization"] = relationship(
        "Organization",
        back_populates="founder",
        uselist=False,
    )

    role_id: Mapped[UUID] = mapped_column(ForeignKey("roles.id"), nullable=True)
    role: Mapped["Role"] = relationship(
        "Role",
        foreign_keys=role_id,
        back_populates="users",
    )
    posts: Mapped[list["Posts"]] = relationship(
        "Post",
        back_populates="user", cascade="all, delete-orphan"
    )
