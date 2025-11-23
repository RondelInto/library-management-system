from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db import Base
import enum
from datetime import datetime

class UserRole(str, enum.Enum):
    admin = "admin"
    user = "user"

class TransactionType(str, enum.Enum):
    borrow = "borrow"
    return_ = "return"

class TransactionStatus(str, enum.Enum):
    active = "active"
    overdue = "overdue"
    returned = "returned"

class ReadingStatus(str, enum.Enum):
    reading = "reading"
    completed = "completed"

class Priority(str, enum.Enum):
    High = "High"
    Medium = "Medium"
    Low = "Low"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.user)
    created_at = Column(DateTime, default=datetime.utcnow)

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    description = Column(Text)
    isbn = Column(String(13), unique=True)
    pages = Column(Integer)
    publish_year = Column(Integer)
    rating_avg = Column(Float, default=0.0)
    rating_count = Column(Integer, default=0)
    copies_total = Column(Integer, default=1)
    copies_available = Column(Integer, default=1)
    genre = Column(String(100))
    cover_url = Column(String(500))
    preloaded = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    type = Column(Enum(TransactionType))
    status = Column(Enum(TransactionStatus), default=TransactionStatus.active)
    due_date = Column(DateTime)
    borrow_date = Column(DateTime, default=datetime.utcnow)
    return_date = Column(DateTime, nullable=True)
    fine_amount = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User")
    book = relationship("Book")

class Wishlist(Base):
    __tablename__ = "wishlists"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    added_at = Column(DateTime, default=datetime.utcnow)

class ReadingProgress(Base):
    __tablename__ = "reading_progress"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    current_page = Column(Integer, default=0)
    percent_complete = Column(Float, default=0.0)
    status = Column(Enum(ReadingStatus), default=ReadingStatus.reading)
    started_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    rating = Column(Float)
    review_text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String(255))
    body = Column(Text)
    priority = Column(Enum(Priority), default=Priority.Medium)
    read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class ReportsLog(Base):
    __tablename__ = "reports_log"
    id = Column(Integer, primary_key=True, index=True)
    admin_user_id = Column(Integer, ForeignKey("users.id"))
    report_type = Column(String(50))
    filters_json = Column(Text)
    generated_at = Column(DateTime, default=datetime.utcnow)
    file_path = Column(String(500), nullable=True)
    record_count = Column(Integer)