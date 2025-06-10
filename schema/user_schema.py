from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[int] = Field(default=None, description="Unique identifier for the user")
    username: str = Field(..., min_length=3, max_length=100, description="Username of the user")
    phone: str = Field(..., min_legth=10, max_length=20, description="Email address of the user")
  
  
    
    #class Config:
    #    orm_mode = True
    #    schema_extra = {
    #        "example": {
    #            "id": 1,
    #            "username": "johndoe",
    #            "email": "