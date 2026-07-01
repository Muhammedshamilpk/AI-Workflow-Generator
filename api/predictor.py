import joblib
import json
from pathlib import Path
import sys
import sklearn

print("Python Executable:", sys.executable)
print("Scikit-learn Version:", sklearn.__version__)

BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"
DATA_DIR = BASE_DIR / "data"

trigger_pipeline = joblib.load(
    MODELS_DIR / "trigger_pipeline.pkl"
)

print("Trigger pipeline:", trigger_pipeline)
print("Pipeline steps:", trigger_pipeline.named_steps)

tfidf = trigger_pipeline.named_steps["tfidf"]

print("TF-IDF type:", type(tfidf))
print("Has idf_:", hasattr(tfidf, "idf_"))

if hasattr(tfidf, "idf_"):
    print("Vocabulary size:", len(tfidf.vocabulary_))

trigger_encoder = joblib.load(
    MODELS_DIR / "trigger_label_encoder.pkl"
)

action_pipeline = joblib.load(
    MODELS_DIR / "action_pipeline.pkl"
)

action_encoder1  = joblib.load(
    MODELS_DIR / "action_encoder1.pkl"
)

action_encoder2 = joblib.load(
    MODELS_DIR / "action_encoder2.pkl"
)

action_encoder3 = joblib.load(
    MODELS_DIR / "action_encoder3.pkl"
)



print(BASE_DIR)
print(MODELS_DIR)
print(MODELS_DIR / "trigger_pipeline.pkl")

with open(DATA_DIR / "workflow_rules.json","r") as f:
    workflow_rules = json.load(f)
    
def predict_workflow(text:str):
    
    trigger_prediction = trigger_pipeline.predict([text])

    trigger = trigger_encoder.inverse_transform(
        trigger_prediction
    )[0]
    
    action_prediction = action_pipeline.predict([text])

    action1 = action_encoder1.inverse_transform(
    [action_prediction[0][0]]
    )[0]

    action2 = action_encoder2.inverse_transform(
    [action_prediction[0][1]]
    )[0]

    action3 = action_encoder3.inverse_transform(
    [action_prediction[0][2]]
    )[0]

    predicted_actions = [action1,action2,action3]
    
    allowed_actions = workflow_rules[trigger]


    final_actions = []

    for action in predicted_actions:
        if action == "None":
            continue
        
        if action in allowed_actions:
            final_actions.append(action)
            
    final_actions = list(dict.fromkeys(final_actions))
        
    workflow = {
        "trigger":trigger,
        "actions":final_actions
    }
    return workflow
