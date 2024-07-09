from pydantic import BaseModel
from typing import List, Optional


class SignUp(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    password: str
    is_active: bool
    is_staff: bool

    class Config:
        orm_mode = True
        json_schema_extra = {
            "example": {
                "username": "samariddin",
                "email": "samariddimn7444@gmai.com",
                "password": "samariddin7444",
                "is_active": True,
                "is_staff": False,
            }
        }

class Login(BaseModel):
    username_or_email: str
    password: str