from fastapi import FastAPI

from api.schemas import WorkflowRequest
from api.predictor import predict_workflow

app = FastAPI(
    title ="AI Workflow Generator API"
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