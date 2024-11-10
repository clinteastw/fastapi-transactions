from fastapi_users import schemas
from pydantic import EmailStr, BaseModel


class AccountCreate(BaseModel):
    balance: float
    user_id: int
    
class AccountUpdate(AccountCreate):
    balance: float