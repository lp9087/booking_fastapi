from sqlalchemy import Column, Integer, Boolean, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from core.database import Base


class Tables(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer, unique=True)
    seats = Column(Integer)
    status = Column(Boolean, default=True)
    booking = relationship("Booking", back_populates="table")


class Queue(Base):
    __tablename__ = "queue"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    guest_number = Column(Integer)
    phone_number = Column(Integer)
    datetime = Column(DateTime)
    note = Column(String)
    status = Column(Boolean, default=False)
    booking = relationship("Booking", back_populates="quest")


class Booking(Base):
    __tablename__ = "booking"
    id = Column(Integer, primary_key=True, autoincrement=True)
    table_num = Column(Integer, ForeignKey('tables.number'))
    table = relationship("Tables", back_populates="booking")
    quest_id = Column(Integer, ForeignKey('queue.id'))
    quest = relationship("Queue", back_populates="booking")
    beginning_time = Column(DateTime)
    ending_time = Column(DateTime)




