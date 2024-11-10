from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import String, Boolean, select
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload
from sqlalchemy.sql import func
from models.account import Account
from models.user import User
from .schemas import AccountCreate, AccountUpdate
from auth.auth import current_user


async def get_accounts(session: AsyncSession, user_id: int):
    stmt = (select(User)
            .options(selectinload(User.accounts))
            .where(User.id == user_id)
            )
    result = await session.execute(stmt)
    accounts = result.scalars().all()
    return accounts
    

# async def get_accounts(session: AsyncSession):
#     stmt = select(User).options()


async def create_account(session: AsyncSession, account_in: AccountCreate):
    account = Account(**account_in.model_dump())
    session.add(account)
    await session.commit()
    return account
    
    
# async def check_or_create_account(session: AsyncSession, account_in: AccountCreate):
    

# async def update_account_balance(
#     session: AsyncSession,
#     account_in: AccountUpdate
#     ):
    
    