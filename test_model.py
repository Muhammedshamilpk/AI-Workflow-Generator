import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"

pipeline = joblib.load(MODELS_DIR / "trigger_pipeline.pkl")

print(pipeline)

print("\nTrying prediction...\n")

print(
    pipeline.predict(
        ["When a customer signs up, send an email"]
    )
)