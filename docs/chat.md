# Looi Interaction

The `chat.py` script provided here enables interaction with a trained chatbot model using the command line interface. This README explains the chatting process, its usage, the packages utilized, and the functions involved, along with customization options.

## Chatting Process

1. **Initialization:**
   - Load the intents data from `intents.json` to understand user queries and provide appropriate responses.
   - Load the trained model parameters and necessary metadata from the `data.pth` file.

2. **User Interaction:**
   - Prompt the user to input queries or messages.
   - Tokenize the user input into words.
   - Convert the input into a bag of words representation using the vocabulary derived from the training data.

3. **Model Prediction:**
   - Pass the bag of words representation through the trained neural network model to predict the intent or category of the user input.
   - Compute the probability of the predicted intent.

4. **Response Generation:**
   - If the predicted intent has a high probability (> 0.75), randomly select a response from the corresponding intent in the intents data.
   - If the probability is lower, respond with a generic "I do not understand..." message.

5. **Continued Interaction:**
   - Repeat the above steps until the user decides to quit the chat session by typing "quit".

## Usage

1. **Chatting:**
   - Run the `chat.py` script using Python.
   - Interact with the chatbot by typing messages or queries when prompted.
   - The chatbot will respond with appropriate answers based on the trained model.

2. **Exiting:**
   - Type "quit" to exit the chat session.

## Packages Used

- **torch**: PyTorch library for loading and using the trained neural network model.
- **json**: For loading and parsing the intents data from `intents.json`.
- **random**: For randomly selecting responses from the intents data.
- **nltk_utils**: Custom utility functions for tokenization and bag of words representation.
- **model**: Definition of the neural network model used for inference.

## Functions

- **tokenize(sentence)**: Tokenizes the input sentence into words.
- **bag_of_words(tokenized_sentence, all_words)**: Converts the tokenized sentence into a bag of words representation using the vocabulary derived from the training data.

## Customization

- **Response Customization**: Modify the responses in the `intents.json` file to tailor the chatbot's replies to specific queries or scenarios.
- **Intent Expansion**: Add new intents, patterns, and responses to the `intents.json` file to enhance the chatbot's capabilities.
- **Model Customization**: Experiment with different neural network architectures or hyperparameters for training a custom chatbot model.
- **User Interface**: Extend the chatbot to interact with users through other channels, such as web interfaces or messaging platforms.

---

This README provides detailed information about the chatbot interaction process, including its implementation, usage, customization options, and potential contributions. Feel free to further enhance it as needed!