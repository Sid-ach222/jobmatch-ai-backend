from fastapi import FastAPI
from routes import candidate_routes, company_routes
from routes import predict_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS if frontend is running on different port
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include candidate routes
app.include_router(candidate_routes.router)
app.include_router(company_routes.router)
app.include_router(predict_routes.router)

@app.get("/")
def root():
    return {"message": "JobMatch AI Backend Running"}
