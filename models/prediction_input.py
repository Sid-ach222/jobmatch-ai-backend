from pydantic import BaseModel

class PredictionInput(BaseModel):
    education: str
    experience: float
    skills: str
    job_title: str
    location: str
