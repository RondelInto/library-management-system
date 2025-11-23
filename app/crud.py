from typing import Optional
from sqlalchemy.orm import Session
from app.models import User, Book, Transaction, Wishlist, ReadingProgress, Review, Notification, ReportsLog
from app.schemas import UserCreate, BookCreate, TransactionCreate, WishlistCreate, ReadingProgressUpdate, ReviewCreate, NotificationCreate
from datetime import datetime

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()

def create_book(db: Session, book: BookCreate):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def create_transaction(db: Session, transaction: TransactionCreate):
    db_transaction = Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def update_book_copies(db: Session, book_id: int, delta: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        book.copies_available += delta
        db.commit()

def create_wishlist(db: Session, wishlist: WishlistCreate):
    db_wishlist = Wishlist(**wishlist.dict())
    db.add(db_wishlist)
    db.commit()
    db.refresh(db_wishlist)
    return db_wishlist

def update_reading_progress(db: Session, progress: ReadingProgressUpdate):
    db_progress = db.query(ReadingProgress).filter(
        ReadingProgress.user_id == progress.user_id,
        ReadingProgress.book_id == progress.book_id
    ).first()
    if not db_progress:
        db_progress = ReadingProgress(**progress.dict())
        db.add(db_progress)
    else:
        for key, value in progress.dict().items():
            setattr(db_progress, key, value)
        db_progress.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_progress)
    return db_progress

def create_review(db: Session, review: ReviewCreate):
    db_review = Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def create_notification(db: Session, notification: NotificationCreate):
    db_notification = Notification(**notification.dict())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

def get_unread_notifications_count(db: Session, user_id: int):
    return db.query(Notification).filter(Notification.user_id == user_id, Notification.read == False).count()

def log_report(db: Session, admin_user_id: int, report_type: str, filters_json: str, record_count: int, file_path: Optional[str] = None):
    db_log = ReportsLog(
        admin_user_id=admin_user_id,
        report_type=report_type,
        filters_json=filters_json,
        record_count=record_count,
        file_path=file_path
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log