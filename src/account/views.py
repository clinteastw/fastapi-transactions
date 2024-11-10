from fastapi import APIRouter, Depends
from . import crud
from .schemas import AccountCreate
from database import get_async_session

from sqlalchemy.ext.asyncio import AsyncSession
from models.account import Account
from models.user import User
from auth.auth import current_user


router = APIRouter(tags=["Accounts"])


@router.post("/", response_model=None)
async def create_account(
    account_in: AccountCreate,
    session: AsyncSession = Depends(get_async_session)
):
    return await crud.create_account(session=session, account_in=account_in)


@router.get("/")
async def get_accounts(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    return await crud.get_accounts(session=session, user_id=user.id)