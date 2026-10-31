from pydantic import BaseModel, Field
from typing import Optional, Any

class CarCreate(BaseModel):
    car_code: str = Field(..., min_length=4, max_length=10)
    rental_price: float = Field(..., gt=0)
    car_type_id: int

class CarTypeResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class CarResponse(BaseModel):
    id: int
    car_code: str
    rental_price: float
    car_type: CarTypeResponse

    class Config:
        orm_mode = True

class BaseResponse(BaseModel):
    statusCode: int
    error: Optional[str] = None
    message: str
    data: Optional[Any] = None
