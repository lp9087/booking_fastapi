from sqlalchemy.orm import Session

import schemas, models


def get_table(db:Session, number: int):
    return db.query(models.Tables).filter(models.Tables.number == number).first()
