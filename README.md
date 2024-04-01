# Contextual Chatbot in PyTorch

This repository contains an implementation of a contextual chatbot in PyTorch. The chatbot is designed to provide a simple yet effective implementation of a chatbot for a coffee shop.

## Features

- Simple implementation with a Feed Forward Neural network with 2 hidden layers.
- `intents.json` file which is the data which represents the knowledge base of the AI model.
- Inspired by the article ["Contextual Chat Bots with TensorFlow"](https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077) and ported to PyTorch.

## Installation

1. **Create a Python environment:**

    You can use any method you prefer to create a virtual environment. Here's an example using `venv`:

    ```bash
    mkdir looi
    cd looi
    python3 -m venv venv
    ```

2. **Activate the environment:**

    - Mac / Linux:
      ```bash
      . venv/bin/activate
      ```
    - Windows:
      ```bash
      venv\Scripts\activate
      ```

3. **Install PyTorch and dependencies:**

    Visit the [official PyTorch website](https://pytorch.org/) for installation instructions.
    Install PyTorch:

    ```bash
    pip install torch
    ```

    Additionally, install NLTK (Natural Language Toolkit):

    ```bash
    pip install nltk
    ```

    If you encounter an error during the first run, you may need to install the `punkt` tokenizer by running the following commands in your terminal:

    ```bash
    python
    >>> import nltk
    >>> nltk.download('punkt')
    ```

## Usage

1. **Training:**

    Run the following command to train looi:

    ```bash
    python train.py
    ```

    This will create a `data.pth` file.

2. **Chatting:**

    After training, you can interact with looi by running:

    ```bash
    python chat.py
    ```

## Customization

To customize the chatbot for specific use case:

1. **Modify `intents.json`:**

    Open the `intents.json` file and define new tags, possible patterns, and responses according to your needs.

    Example snippet from `intents.json`:

    ```json
    {
      "intents": [
        {
          "tag": "greeting",
          "patterns": [
            "Hi",
            "Hey",
            "How are you",
            "Is anyone there?",
            "Hello",
            "Good day"
          ],
          "responses": [
            "Hey :-)",
            "Hello, thanks for visiting",
            "Hi there, what can I do for you?",
            "Hi there, how can I help?"
          ]
        },
        ...
      ]
    }
    ```

2. **Re-run training:**

    After modifying `intents.json`, re-run the training script:

    ```bash
    python train.py
    ```



