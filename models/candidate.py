from pydantic import BaseModel, EmailStr
from typing import List, Optional

class Candidate(BaseModel):
    name: str
    email: EmailStr
    education: str
    experience_years: float
    skills: List[str]
    applied_role: str
    location: str
    resume_text: Optional[str] = None
