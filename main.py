import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from auth import security

app = FastAPI()


class User(BaseModel):
    login: str
    password: str


@app.get("/login-user")
async def login_user(data: User):
    newclass = security.CustomSecurity()
    message = newclass.check_user(data.login, data.password)
    return message


@app.get("/create-user")
async def create_user(data: User):
    newclass = security.CustomSecurity()
    newclass.registration_new_user(data.login, data.password)
    return f"ok"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
