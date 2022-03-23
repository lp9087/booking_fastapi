from typing import Optional

from pydantic import BaseModel


class Table(BaseModel):
    number: int
    seats: int
    status: Optional[bool] = True

    class Config:
        orm_mode = True


class UpdateTable(BaseModel):
    seats: int

    class Config:
        orm_mode = True