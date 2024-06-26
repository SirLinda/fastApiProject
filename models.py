from enum import Enum
from typing import Optional, List
from uuid import UUID, uuid4

from pydantic import BaseModel


class Gender(str, Enum):
    MALE = "Male"
    FEMALE = "Female"


class Role(str, Enum):
    ADMIN = "Admin"
    STUDENT = "Student"
    USER = "User"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: str
    gender: Gender
    roles: List[Role]
