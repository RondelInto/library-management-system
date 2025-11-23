from app.db import SessionLocal
from app.crud import create_user, create_book
from app.schemas import UserCreate, BookCreate

def seed_data():
    db = SessionLocal()
    try:
        # Sample users
        create_user(db, UserCreate(name="Admin User", email="admin@example.com", role="admin"))
        create_user(db, UserCreate(name="John Doe", email="john@example.com"))
        create_user(db, UserCreate(name="Jane Smith", email="jane@example.com"))

        # Sample books
        books_data = [
            {"title": "1984", "author": "George Orwell", "isbn": "9780451524935", "pages": 328, "publish_year": 1949, "genre": "Dystopian", "cover_url": "https://example.com/1984.jpg", "preloaded": True},
            {"title": "To Kill a Mockingbird", "author": "Harper Lee", "isbn": "9780061120084", "pages": 376, "publish_year": 1960, "genre": "Fiction", "cover_url": "https://example.com/mockingbird.jpg", "preloaded": True},
            # Add 8 more similar entries...
        ]
        for book in books_data:
            create_book(db, BookCreate(**book))
        print("Seeded data successfully.")
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()