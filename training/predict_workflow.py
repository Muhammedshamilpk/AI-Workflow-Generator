import joblib
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"
DATA_DIR = BASE_DIR / "data"

trigger_pipeline = joblib.load(
    MODELS_DIR / "trigger_pipeline.pkl"
)

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


with open(DATA_DIR / "E:\PROJECTS\AI-Workflow-Generator\data\workflow_rules.json","r") as f:
    workflow_rules = json.load(f)
    
while True:
    text = input("\nDescribe your Workflow: ")
    
    if text.lower()=="exit":
        break
    
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

    allowed_actions = workflow_rules[trigger]

    predicted_actions = [
    action1,
    action2,
    action3
    ]

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

    print("\nGenerated Workflow:\n")

    print(json.dumps(
        workflow,
        indent=4
    ))