from sqlalchemy.orm import Session
from app.schemas import ReportRequest

def preview_count(db: Session, request: ReportRequest):
    return {"record_count": 0, "report_type": request.report_type}

def generate_report(db: Session, request: ReportRequest):
    return {"success": True, "message": "Report generated"}