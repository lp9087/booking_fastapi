from pydantic import BaseModel


class Table(BaseModel):
    number: int
    seats: int

    class Config:
        orm_mode = True