import json
import pandas as pd

# Load intents from JSON file
with open('intents.json', 'r') as file:
    intents_data = json.load(file)

# Create empty lists to store data
tags = []
patterns = []
responses = []

# Extract data from intents
for intent in intents_data['intents']:
    tag = intent['tag']
    tags.extend([tag] * 3)  # Repeat tag 3 times
    patterns.extend(intent['patterns'][:3])  # Limit to 3 patterns per intent
    responses.extend(intent['responses'][:3])  # Limit to 3 responses per intent

# Create a DataFrame from the extracted data
intents_df = pd.DataFrame({'Tag': tags, 'Pattern': patterns, 'Response': responses})

# Display the DataFrame
print(intents_df.to_string(index=False))
