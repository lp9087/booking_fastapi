from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import crud
import models
import tables_router
from core.database import engine, SessionLocal
from schemas import Table

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.include_router(tables_router.router)


@app.get("/", response_model=Table)
def tables(number: int, seats: int, db: Session = Depends(get_db)):
    tables = crud.get_table(db, number=number, seats=seats)
    return tables