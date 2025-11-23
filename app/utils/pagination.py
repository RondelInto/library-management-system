from sqlalchemy.orm import Session
from app.models import Book
from app.schemas import BookSearch, PaginatedBooks


def paginate_books(db: Session, search: BookSearch):
    query = db.query(Book)

    if search.q:
        query = query.filter(Book.title.ilike(f"%{search.q}%") | Book.author.ilike(f"%{search.q}%"))
    if search.genre:
        query = query.filter(Book.genre == search.genre)

    total_count = query.count()
    books = query.offset((search.page - 1) * search.limit).limit(search.limit).all()

    return PaginatedBooks(
        books=[{
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
            "copies_available": book.copies_available,
            "rating_avg": book.rating_avg
        } for book in books],
        total_count=total_count
    )