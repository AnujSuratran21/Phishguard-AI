from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.scan import Scan

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


# GET ALL HISTORY
@router.get("/")
def get_history(
    db: Session = Depends(get_db)
):

    scans = db.query(Scan).all()

    return scans


# CLEAR ALL HISTORY
@router.delete("/clear")
def clear_history(
    db: Session = Depends(get_db)
):

    db.query(Scan).delete()

    db.commit()

    return {
        "message": "All scan history cleared"
    }
