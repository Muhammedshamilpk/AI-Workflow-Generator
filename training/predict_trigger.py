import joblib

pipline = joblib.load("E:\PROJECTS\AI-Workflow-Generator\models/trigger_pipeline.pkl")
encoder = joblib.load("E:\PROJECTS\AI-Workflow-Generator\models/trigger_label_encoder.pkl")

print("="*50)
print("AI Workflow Trigger Prediction")
print("Type 'exit' to quit")
print("=" *50)

while True:
    text = input ("\nEnter Workflow Description:")
    
    if text.lower()== "exit":
        print("\nGoodBye!")
        break
    prediction = pipline.predict([text])
    
    trigger = encoder.inverse_transform(prediction)
    
    print(f"\nPredicted Trigger: {trigger[0]}")