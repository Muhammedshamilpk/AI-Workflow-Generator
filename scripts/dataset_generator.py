import json
import pandas as pd
import random
from pathlib import Path

random.seed(42)

BASE_DIR =Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = DATA_DIR / "processed"
OUTPUT_DIR.mkdir(exist_ok=True)

# with open(DATA_DIR/"trigger_templates.json","r") as f:
#     triggers = json.load(f)
    
with open(DATA_DIR/"action_templates.json","r") as f:
    actions = json.load(f)
    
with open(DATA_DIR/"trigger_templates.json","r") as f:
    templates = json.load(f)

with open(DATA_DIR / "workflow_rules.json","r") as f:
    workflow_rules = json.load(f)


dataset=[]

record_id = 1

seen=set()

for trigger,trigger_templates in templates.items():
    
    allowed_actions = workflow_rules[trigger]
    
    for _ in range(10):    
        
        for trigger_sentence in trigger_templates:
            
            num_actions = random.randint(1,min(3,len(allowed_actions)))
            
            selected_actions = sorted(random.sample(
                allowed_actions,
                num_actions
            )
            )
        
            selected_action_sentences =[]
                
            for action in selected_actions:
                        
                action_templates = actions[action]
                action_sentence = random.choice(action_templates)
                selected_action_sentences.append(action_sentence)

            if len(selected_action_sentences) == 1:
                action_text = selected_action_sentences[0]
            else:
                action_text = ", ".join(selected_action_sentences[:-1])
                action_text+= " and " + selected_action_sentences[-1]
                
            sentence = f"{trigger_sentence}, {action_text}."
                
            if sentence in seen   :
                continue
            seen.add(sentence)
                                
                                
            dataset.append(
                            {
                            "id":record_id,
                            "user_input":sentence,
                            "trigger":trigger,
                            "action_1":selected_actions[0] if len(selected_actions) > 0 else "",
                            "action_2":selected_actions[1] if len(selected_actions) > 1 else "",
                            "action_3":selected_actions[2] if len(selected_actions) >2 else ""                        }
                            )
            record_id +=1

df = pd.DataFrame(dataset)


df.to_csv(
        OUTPUT_DIR / "workflow_dataset.csv",
        index=False
    )
print(df.head(10))

print(len(templates))
print(len(df))
print(templates.keys())