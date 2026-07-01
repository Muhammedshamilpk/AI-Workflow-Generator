import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.multioutput import MultiOutputClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"

MODELS_DIR.mkdir(exist_ok=True)

df = pd.read_csv("E:\PROJECTS\AI-Workflow-Generator\data\processed\workflow_dataset.csv")
print(df.head())

df["action_1"]=df["action_1"].fillna("None")
df["action_2"]=df["action_2"].fillna("None")
df["action_3"]=df["action_3"].fillna("None")

X=df["user_input"]

encoder1 = LabelEncoder()
encoder2 = LabelEncoder()
encoder3 = LabelEncoder()

y1 = encoder1.fit_transform(df["action_1"])
y2 = encoder2.fit_transform(df["action_2"])
y3 = encoder3.fit_transform(df["action_3"])

import numpy as np 

Y=np.column_stack((y1,y2,y3))

X_train,X_test,Y_train,Y_test = train_test_split(
    X,Y,test_size=0.2,random_state=42
)

MultiOutputClassifier(
    LogisticRegression(max_iter=100)
)

pipeline = Pipeline([
    ("tfidf",TfidfVectorizer()),
    (
        "classifier",
        MultiOutputClassifier(
            LogisticRegression(max_iter=100)
        )
    )
]
)

pipeline.fit(X_train,Y_train)

predictions = pipeline.predict(X_test)

pred_action1 = encoder1.inverse_transform(predictions[:,0])
pred_action2 = encoder2.inverse_transform(predictions[:,1])
pred_action3 = encoder3.inverse_transform(predictions[:,2])

print("\nSample Predictions\n")

for i in range(10):
    print("Input :",X_test.iloc[i])
    
    print("Predicted Actions :")
    
    print(pred_action1[i])
    print(pred_action2[i])
    print(pred_action3[i])
    
    print("-"*50)
    
joblib.dump(
    pipeline,
    MODELS_DIR /"action_pipeline.pkl"
)

joblib.dump(
    encoder1,
    MODELS_DIR /"action_encoder1.pkl"
)

joblib.dump(
    encoder2,
    MODELS_DIR /"action_encoder2.pkl"
)

joblib.dump(
    encoder3,
    MODELS_DIR /"action_encoder3.pkl"
)

print("\nAction Model Saved Successfully")