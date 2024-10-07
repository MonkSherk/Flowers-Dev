from pydantic import BaseModel, EmailStr


class uAuth(BaseModel):
    name: str
    mail: EmailStr
    password: str