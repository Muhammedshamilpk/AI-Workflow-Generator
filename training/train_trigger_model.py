import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report


BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"

MODELS_DIR.mkdir(exist_ok=True)

df = pd.read_csv("E:\PROJECTS\AI-Workflow-Generator\data\processed\workflow_dataset.csv")

print("Dataset Shape:",df.shape)


X = df["user_input"]
y = df["trigger"]

encoder = LabelEncoder()
y=encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size = 0.2, stratify = y
)

pipeline = Pipeline([
    ("tfidf",TfidfVectorizer()),
    ("classifier",LogisticRegression(max_iter=1000))
])

pipeline.fit(X_train,y_train)

predictions = pipeline.predict(X_test)

accuracy = accuracy_score(y_test,predictions)

print("\nAccuracy:",accuracy)
print("\nClassification Report:\n")

print(classification_report(
    y_test,
    predictions,
    target_names=encoder.classes_
))

#Save model

joblib.dump(
    pipeline,
   MODELS_DIR / "trigger_pipeline.pkl"
)

joblib.dump(
    encoder,
    MODELS_DIR /"trigger_label_encoder.pkl"
)

print("\nTrigger model saved successfully")