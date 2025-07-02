from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pandas as pd
import pickle

router = APIRouter()

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

class CandidateInput(BaseModel):
    job_category: str
    experience_years: int
    skills: str
    job_title: str
    job_type: str
    education: str
    location: str

@router.post("/predict")
async def predict(data: CandidateInput):
    try:
        input_dict = data.dict()
        input_df = pd.DataFrame([input_dict])
        print("Received input:\n", input_df)

        prediction = model.predict_proba(input_df)
        print("Prediction output:", prediction)

        probability = prediction[0][1]  # hiring probability
        return {"prediction": float(probability)}

    except Exception as e:
        print("Prediction error:", str(e))
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
