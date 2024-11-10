from dotenv import load_dotenv
import os

from fastapi import APIRouter, Depends, HTTPException
from . import crud as crud_payment
from account import crud as crud_account
from .schemas import PaymentCreate
from database import get_async_session

from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from models.account import Account
from models.user import User
from auth.auth import current_user


load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")


router = APIRouter(tags=["Payments"])

@router.post("/", response_model=None)
async def create_payment(
    payment_in: PaymentCreate,
    session: AsyncSession = Depends(get_async_session)
):
    
    payment_details = payment_in.model_dump()
    
    crud_payment.check_signature(payment_details, SECRET_KEY)
    
    stmt = (
        select(Account)
        .where(
            and_(Account.id == payment_details["account_id"],
               Account.user_id == payment_details["user_id"])
            )
    )
    result = await session.execute(stmt)
    account = result.scalar_one_or_none()
        
    if not account:
        user_stmt = select(User).where(id==payment_details["user_id"])
        user_result = await session.execute(user_stmt)
        user = user_result.scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        account = Account(user_id=payment_details["user_id"], balance=0)
        session.add(account)
        await session.commit()
        
    await crud_payment.create_payment(session=session, payment_in=payment_in)
    account.balance += payment_details["amount"]
    await session.commit()
    
    return {"status": "success"}