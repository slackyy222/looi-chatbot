import json
import networkx as nx
import matplotlib.pyplot as plt

# Load intents from JSON file
with open('intents.json', 'r') as file:
    intents = json.load(file)

# Create a directed graph
G = nx.DiGraph()

# Add nodes (intents) to the graph
for intent in intents['intents']:
    G.add_node(intent['tag'])

    # Add edges (patterns and responses) to the graph
    for pattern in intent['patterns']:
        G.add_edge(intent['tag'], pattern)
    for response in intent['responses']:
        G.add_edge(intent['tag'], response)

# Draw the graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, k=0.5)  # Position nodes using Fruchterman-Reingold force-directed algorithm
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold', arrowsize=20)
plt.title('Graphical Representation of Intents in Intents.json')
plt.show()
