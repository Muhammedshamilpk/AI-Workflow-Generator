import pandas as pd

df = pd.read_csv("E:\PROJECTS\AI-Workflow-Generator\data\processed\workflow_dataset.csv")

print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

df["action_2"] = df["action_2"].fillna("")
df["action_3"] = df["action_3"].fillna("")

df.to_csv("E:\PROJECTS\AI-Workflow-Generator\data\processed\workflow_dataset.csv",
          index=False)

print("Preprocessing Completed Successfully")