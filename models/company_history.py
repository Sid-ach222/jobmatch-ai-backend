from pydantic import BaseModel
from typing import List

class CompanyHistory(BaseModel):
    company: str
    job_title: str
    education: str
    experience_years: float
    skills: List[str]
    location: str
    hired: bool  # True if candidate was hired, False if rejected
