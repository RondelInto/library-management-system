from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app.db import get_db
from app.config import Config
from app.schemas import ReportRequest
from app.reports.generator import generate_report, preview_count


router = APIRouter()

def verify_admin(token: str = Header(..., alias="X-Admin-Token")):
    if token != Config.ADMIN_API_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid admin token")

@router.get("/reports/preview-count")
def get_preview_count(request: ReportRequest, db: Session = Depends(get_db), token: str = Depends(verify_admin)):
    return preview_count(db, request)

@router.post("/reports/generate")
def generate_report_endpoint(request: ReportRequest, db: Session = Depends(get_db), token: str = Depends(verify_admin)):
    return generate_report(db, request)
