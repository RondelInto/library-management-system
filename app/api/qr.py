import time
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.crud import create_transaction, update_book_copies
from app.schemas import QRScanRequest, TransactionCreate
from datetime import datetime, timedelta

router = APIRouter()

@router.post("/scan")
def scan_qr(request: QRScanRequest, db: Session = Depends(get_db)):
    # Simulate delay
    time.sleep(2)
    # Stub: Assume code is "book_<id>_borrow" or "book_<id>_return"
    parts = request.code.split("_")
    if len(parts) != 3:
        return {"success": False, "message": "Invalid QR code"}
    book_id = int(parts[1])
    action = parts[2]
    user_id = 1  # Stub user
    if action == "borrow":
        transaction = TransactionCreate(user_id=user_id, book_id=book_id, type="borrow", due_date=datetime.utcnow() + timedelta(days=14))
        create_transaction(db, transaction)
        update_book_copies(db, book_id, -1)
    elif action == "return":
        # Logic to update transaction status
        pass
    return {"success": True, "message": f"{action.capitalize()} successful"}