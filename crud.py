from fastapi import HTTPException
from sqlalchemy.orm import Session

import schemas, models


def get_table(db: Session, table_num: int):
    return db.query(models.Tables).filter(models.Tables.number == table_num).first()


def get_tables(db: Session, skip: int, limit: int):
    return db.query(models.Tables).offset(skip).limit(limit).all()


def create_table(db: Session, table: schemas.Table):
    db_table = models.Tables(number=table.number, seats=table.seats, status=table.status)
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table


def delete_table(db: Session, table_num: int):
    table = db.query(models.Tables).filter(models.Tables.number == table_num).first()
    if not table:
        return None
    db.query(models.Tables).filter(models.Tables.number == table_num).delete()
    db.commit()
    return True


def update_table(db: Session, table_num: int, table: schemas.UpdateTable):
    db_table = get_table(db=db, table_num=table_num)
    if not db_table:
        return None
    db_table.seats = table.seats
    db.commit()
    db.refresh(db_table)
    return db_table


def create_queue(db: Session, queue: schemas.Queue):
    db_queue = models.Queue(
        name=queue.name,
        guest_number=queue.guest_number,
        phone_number=queue.phone_number,
        datetime=queue.datetime,
        note=queue.note,
        status=queue.status)
    db.add(db_queue)
    db.commit()
    db.refresh(db_queue)
    return db_queue


def get_queues(db: Session):
    return db.query(models.Queue).all()


def create_booking(db: Session, booking: schemas.CreateBooking):
    db_booking = models.Booking(table_num=booking.table_num, quest_id=booking.quest_id)
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking


def get_booking(db: Session):
    return db.query(models.Booking).all()