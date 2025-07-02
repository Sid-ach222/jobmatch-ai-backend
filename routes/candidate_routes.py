from fastapi import APIRouter, HTTPException
from models.candidate import Candidate
from database.mongodb import candidate_collection
from bson import ObjectId

router = APIRouter()

# Helper to convert BSON to JSON
def serialize_candidate(candidate) -> dict:
    return {
        "id": str(candidate["_id"]),
        "name": candidate["name"],
        "email": candidate["email"],
        "education": candidate["education"],
        "experience_years": candidate["experience_years"],
        "skills": candidate["skills"],
        "applied_role": candidate["applied_role"],
        "location": candidate["location"],
        "resume_text": candidate.get("resume_text", "")
    }

@router.post("/candidate")
def create_candidate(candidate: Candidate):
    candidate_dict = candidate.dict()
    result = candidate_collection.insert_one(candidate_dict)
    candidate_dict["id"] = str(result.inserted_id)
    return {"message": "Candidate created", "id": candidate_dict["id"]}

@router.get("/candidate/{candidate_id}")
def get_candidate(candidate_id: str):
    candidate = candidate_collection.find_one({"_id": ObjectId(candidate_id)})
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return serialize_candidate(candidate)
