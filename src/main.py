import uvicorn

from fastapi import FastAPI, Depends
from pydantic import BaseModel

from auth.auth import auth_backend, fastapi_users, current_active_user
from auth.schemas import UserRead, UserCreate, UserUpdate
from account.views import router as account_routers
from payment.views import router as payment_routers

from database import User

app = FastAPI(
    title="Transactions App"
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

app.include_router(
    account_routers,
    prefix="/accounts",
)

app.include_router(
    payment_routers,
    prefix="/payments",
)

@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.username}!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)









