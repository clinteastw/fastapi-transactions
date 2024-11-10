from typing import TYPE_CHECKING
import datetime

from .base import Base

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

if TYPE_CHECKING:
    from .account import Account 


class User(Base, SQLAlchemyBaseUserTable[int]):
    
    __tablename__ = "users"
    
    username: Mapped[str] = mapped_column(nullable=False)
    registered_at: Mapped[datetime.datetime] = mapped_column(default=func.now())
    
    email: Mapped[str] = mapped_column(
            String(length=320), unique=True, index=True, nullable=False
        )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    accounts: Mapped[list["Account"]] = relationship(back_populates="user", lazy="selectin")