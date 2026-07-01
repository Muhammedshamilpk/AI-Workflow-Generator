import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"

pipeline = joblib.load(MODELS_DIR / "action_pipeline.pkl")

print(pipeline)

print(
    pipeline.predict(
        ["When a customer signs up, send an email"]
    )
)