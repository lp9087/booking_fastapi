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



