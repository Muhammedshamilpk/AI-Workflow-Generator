from pydantic import BaseModel

class WorkflowRequest(BaseModel):
    text:str
    
class WorkflowResponse(BaseModel):
    trigger:str
    actions:list[str]