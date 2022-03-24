from typing import Optional
from datetime import datetime
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


class Queue(BaseModel):
    name: str
    guest_number: int
    phone_number: int
    datetime: datetime
    note: Optional[str] = None
    status: Optional[bool] = False

    class Config:
        orm_mode = True


class CreateBooking(BaseModel):
    table_num: int
    quest_id: int
    beginning_time = datetime
    ending_time = datetime

    class Config:
        orm_mode = True


class GetBooking(BaseModel):
    table_num: int
    quest_id: int
    beginning_time = datetime
    ending_time = datetime

    class Config:
        orm_mode = True