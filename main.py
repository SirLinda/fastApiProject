from uuid import UUID

from fastapi import FastAPI
from typing import Union, List

from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("d5b7c3a3-be40-4335-8d7c-f9d72c323aa2"),
        first_name="SirLinda",
        last_name="Dev",
        middle_name="DevGod",
        gender=Gender.MALE,
        roles=[Role.ADMIN, Role.USER, Role.STUDENT],

    ),
    User(
        id=UUID("a34bc6dd-a4e2-44a7-a8d8-29e84efadfef"),
        first_name="Nk",
        last_name="Dev",
        middle_name="Rhea",
        gender=Gender.FEMALE,
        roles=[Role.STUDENT],

    )
]


@app.get("/")
async def root():
    return {"message": "Hello Dev"}


@app.get("/api/v1/users")
async def get_users():
    return db


@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}
