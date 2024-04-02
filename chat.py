import torch
import random
import json
import gradio as gr

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

# Load intents and model data
with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

# Extract model parameters
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

# Initialize and load model
model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

bot_name = "Looi"

# Define function to interact with the model
def chat_with_model(sentence, history):
    # Tokenize input sentence
    sentence = tokenize(sentence)

    # Convert input sentence to bag of words
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)

    # Get model prediction
    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    # Generate response
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    else:
        return "I do not understand..."

# Create Gradio interface
iface = gr.ChatInterface(chat_with_model)

# Launch the interface
iface.launch(debug=True, share=True)
