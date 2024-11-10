import datetime

from .base import Base

from sqlalchemy import  ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func


class Payment(Base):
    __tablename__ = "payments"
    
    transaction_id: Mapped[int]
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    amount: Mapped[float]
    time: Mapped[datetime.datetime] = mapped_column(default=func.now())