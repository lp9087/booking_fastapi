from typing import List

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

import crud
from core import services
from schemas import Table, UpdateTable, Queue, Booking

app = FastAPI()

services.create_database()


@app.post("/", tags=['Tables'], response_model=Table, status_code=status.HTTP_201_CREATED)
def create_table(table: Table, db: Session = Depends(services.get_db)):
    return crud.create_table(table=table, db=db)


@app.get("/", tags=['Tables'], response_model=List[Table])
def get_tables(
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(services.get_db)):
    return crud.get_tables(db=db, skip=skip, limit=limit)


@app.get("/{table_num}", tags=['Tables'], response_model=Table)
def get_table(table_num: int, db: Session = Depends(services.get_db)):
    db_table = crud.get_table(table_num=table_num, db=db)
    if not db_table:
        raise HTTPException(status_code=404, detail="Table not found")
    return db_table


@app.put("/{table_num}", tags=['Tables'], response_model=Table)
def update_table(table_num: int, table: UpdateTable,  db: Session = Depends(services.get_db)):
    table = crud.update_table(db=db, table_num=table_num, table=table)
    if not table:
        raise HTTPException(status_code=404, detail="Table not found")
    return crud.update_table(db=db, table_num=table_num, table=table)


@app.delete("/{table_num}", tags=['Tables'], status_code=status.HTTP_205_RESET_CONTENT)
def delete_table(table_num: int, db: Session = Depends(services.get_db)):
    table = crud.delete_table(table_num=table_num, db=db)
    if not table:
        raise HTTPException(status_code=404, detail="Table not found")
    return {"message": f"successfully deleted table {table_num}"}


@app.post("/queue", tags=['Queue'], response_model=Queue, status_code=status.HTTP_201_CREATED)
def create_queue(queue: Queue, db: Session = Depends(services.get_db)):
    return crud.create_queue(queue=queue, db=db)


@app.get("/queue", tags=['Queue'], response_model=List[Queue])
def get_queues(db: Session = Depends(services.get_db)):
    return crud.get_queues(db=db)


@app.post("/booking", tags=['Booking'], response_model=Booking, status_code=status.HTTP_201_CREATED)
def create_booking(booking: Booking, db: Session = Depends(services.get_db)):
    return crud.create_booking(booking=booking, db=db)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)