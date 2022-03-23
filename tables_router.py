from fastapi import APIRouter

router = APIRouter(
    prefix="/api/tables",
    tags=['tables']
)


@router.get("/", )
async def get_tables():
    return 'tables'


@router.get("/{num}", )
async def get_table(num: int):
    return 'table'


@router.post("/{num}", )
async def create_table(num: int):
    return 'table'


@router.delete("/{num}", )
async def delete_table(num: int):
    return 'table'