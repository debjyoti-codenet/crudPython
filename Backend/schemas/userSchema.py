from pydantic import BaseModel, EmailStr
from typing import Optional

class UserRegisterSchema(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str
    
    
# Pydantic -> data validation + structure enforcement

# Ye define karta hai:
# API me incoming data ka format kya hoga
# kaunse fields required hain
# kaunse types allowed hain

class UserUpdateSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None