from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.crud import create_user, create_wishlist, update_reading_progress, create_review
from app.schemas import UserCreate, WishlistCreate, ReadingProgressUpdate, ReviewCreate

router = APIRouter()

@router.post("/")
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.post("/wishlist")
def add_to_wishlist(wishlist: WishlistCreate, db: Session = Depends(get_db)):
    return create_wishlist(db, wishlist)

@router.post("/reading/progress")
def update_progress(progress: ReadingProgressUpdate, db: Session = Depends(get_db)):
    return update_reading_progress(db, progress)

@router.post("/reviews")
def add_review(review: ReviewCreate, db: Session = Depends(get_db)):
    return create_review(db, review)