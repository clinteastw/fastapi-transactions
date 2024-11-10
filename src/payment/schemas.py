from fastapi_users import schemas
from pydantic import EmailStr, BaseModel, Field


class PaymentCreate(BaseModel):
    transaction_id: int
    account_id: int
    user_id: int
    amount: float
    signature: str
    