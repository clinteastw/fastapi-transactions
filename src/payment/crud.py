import hashlib

from fastapi import Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import String, Boolean, select
from sqlalchemy.orm import selectinload
from models.payment import Payment
from .schemas import PaymentCreate
from auth.auth import current_user


async def create_payment(session: AsyncSession, payment_in: PaymentCreate):
    payment = Payment(**payment_in.model_dump(exclude="signature"))
    session.add(payment)
    await session.commit()
    return payment
    
    
def check_signature(data: dict, SECRET_KEY:str):
    signature = f"{data['account_id']}{data['amount']}{data['transaction_id']}{data['user_id']}{SECRET_KEY}"
    expected_signature = hashlib.sha256(signature.encode()).hexdigest()
    
    if data["signature"] != expected_signature:
        raise HTTPException(status_code=400, detail="Invalid signature")