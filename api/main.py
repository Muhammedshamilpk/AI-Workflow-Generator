from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.schemas import WorkflowRequest
from api.predictor import predict_workflow

app = FastAPI(
    title ="AI Workflow Generator API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message":"AI Workflow Generator API is Running"
    }
@app.post("/predict")
def predict(request:WorkflowRequest):
    result = predict_workflow(request.text)
    return result