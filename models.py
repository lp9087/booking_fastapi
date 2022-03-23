from sqlalchemy import Column, Integer, Boolean
from core.database import Base


class Tables(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    number = Column(Integer, unique=True)
    seats = Column(Integer)
    status = Column(Boolean, default=True)
