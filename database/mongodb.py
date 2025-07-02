from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["jobmatch"]
candidate_collection = db["candidates"]
company_history_collection = db["company_history"]
