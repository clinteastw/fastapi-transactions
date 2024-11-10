from typing import TYPE_CHECKING

from .base import Base

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .user import User


class Account(Base):
    
    __tablename__ = "accounts"
    
    balance: Mapped[float]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    
    user: Mapped["User"] = relationship(back_populates="accounts", foreign_keys=[user_id])
    