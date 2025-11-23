from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db import get_db
from app.crud import get_books
from app.utils.pagination import paginate_books
from app.schemas import PaginatedBooks, BookSearch

router = APIRouter()

@router.get("/", response_model=PaginatedBooks)
def search_books(
    q: str = Query(None),
    genre: str = Query(None),
    availability: str = Query(None),
    status: str = Query(None),
    sort: str = Query(None),
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return paginate_books(db, BookSearch(q=q, genre=genre, availability=availability, status=status, sort=sort, page=page, limit=limit))