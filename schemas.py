from pydantic import BaseModel, EmailStr, Field


class CustomerCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    phone: str = Field(..., min_length=1, max_length=15)
    city: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=18)