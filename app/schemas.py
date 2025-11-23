from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.models import TransactionStatus, ReadingStatus, Priority

class UserCreate(BaseModel):
    name: str
    email: str
    role: Optional[str] = "user"

class BookCreate(BaseModel):
    title: str
    author: str
    description: Optional[str]
    isbn: Optional[str]
    pages: Optional[int]
    publish_year: Optional[int]
    copies_total: int = 1
    genre: Optional[str]
    cover_url: Optional[str]
    preloaded: bool = False

class TransactionCreate(BaseModel):
    user_id: int
    book_id: int
    type: str
    due_date: Optional[datetime]

class WishlistCreate(BaseModel):
    user_id: int
    book_id: int

class ReadingProgressUpdate(BaseModel):
    user_id: int
    book_id: int
    current_page: int
    percent_complete: float
    status: ReadingStatus

class ReviewCreate(BaseModel):
    user_id: int
    book_id: int
    rating: float
    review_text: Optional[str]

class NotificationCreate(BaseModel):
    user_id: int
    title: str
    body: str
    priority: Priority = Priority.Medium

class ReportRequest(BaseModel):
    report_type: str  # ALL|ACTIVE|OVERDUE|RETURNED
    date_from: Optional[str]
    date_to: Optional[str]
    format: str  # HTML|CSV

class QRScanRequest(BaseModel):
    code: str

class BookSearch(BaseModel):
    q: Optional[str]
    genre: Optional[str]
    availability: Optional[str]  # available|checkedout
    status: Optional[str]  # reading|completed|wishlist
    sort: Optional[str]  # title|author|rating
    page: int = 1
    limit: int = 10

class PaginatedBooks(BaseModel):
    books: List[dict]
    total_count: int