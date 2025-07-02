from fastapi import APIRouter, HTTPException
from models.company_history import CompanyHistory
from database.mongodb import company_history_collection
from bson import ObjectId

router = APIRouter()

# Serialize Mongo result to JSON
def serialize_record(record) -> dict:
    return {
        "id": str(record["_id"]),
        "company": record["company"],
        "job_title": record["job_title"],
        "education": record["education"],
        "experience_years": record["experience_years"],
        "skills": record["skills"],
        "location": record["location"],
        "hired": record["hired"]
    }

@router.post("/company-history")
def add_history(entry: CompanyHistory):
    result = company_history_collection.insert_one(entry.dict())
    return {"message": "Company hiring record added", "id": str(result.inserted_id)}

@router.get("/company-history/{record_id}")
def get_history(record_id: str):
    record = company_history_collection.find_one({"_id": ObjectId(record_id)})
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    return serialize_record(record)
