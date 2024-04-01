# Looi Training

The `train.py` script provided here is used to train a chatbot model using the data from `intents.json`. This README explains the training process, the rationale behind it, its usage, the packages utilized, and how it can be further customized.

## Training Process

1. **Data Preparation:**
   - Load the intents data from `intents.json`.
   - Extract patterns and tags from the intents data.
   - Tokenize the patterns into words and stem them.
   - Create a bag of words representation for each pattern.
   - Prepare training data by assigning labels to patterns and converting them into numpy arrays.

2. **Model Initialization:**
   - Define hyperparameters such as number of epochs, batch size, learning rate, input size, hidden size, and output size.
   - Implement a custom dataset class `ChatDataset` to handle the training data.
   - Initialize a neural network model (`NeuralNet`) with the specified input, hidden, and output sizes.

3. **Training Loop:**
   - Define the loss function (CrossEntropyLoss) and optimizer (Adam).
   - Iterate over the training data for the specified number of epochs.
   - Perform forward pass through the model.
   - Compute loss and perform backward pass to update model parameters.
   - Print training progress and loss at regular intervals.

4. **Model Saving:**
   - Save the trained model state, along with necessary metadata such as input words, tags, and model parameters, into a `.pth` file (`data.pth`).

## Thought Process

- **Data Preprocessing:** Tokenization and stemming are performed to standardize the input text data and reduce dimensionality.
- **Model Architecture:** A simple Feed Forward Neural Network with one hidden layer is chosen for its simplicity and suitability for the task.
- **Loss Function:** CrossEntropyLoss is used as it is suitable for multi-class classification tasks like ours.
- **Optimizer:** Adam optimizer is chosen for its adaptive learning rate properties, which can lead to faster convergence.

## Usage

1. **Data Preparation:**
   - Ensure that the `intents.json` file contains relevant intents, patterns, and responses for the chatbot training.
   - Modify or extend the data in `intents.json` as needed to customize the chatbot's behavior.

2. **Training:**
   - Run the `train.py` script using Python.
   - Monitor the training progress and loss printed during the training process.
   - Once training is complete, the trained model will be saved as `data.pth`.

## Packages Used

- **numpy**: For numerical computations and array manipulations.
- **torch**: PyTorch library for building and training neural networks.
- **nltk**: Natural Language Toolkit for text preprocessing tasks such as tokenization and stemming.

## Customization

- **Data Customization:** Modify the `intents.json` file to include additional intents, patterns, and responses relevant to your specific use case.
- **Model Architecture:** Experiment with different neural network architectures, such as adding more hidden layers or using different activation functions.
- **Hyperparameters:** Adjust hyperparameters such as learning rate, batch size, and number of epochs for optimal model performance.

---

This README provides detailed information about the training process for the chatbot model, including its implementation, usage, customization options, and potential contributions. Feel free to further enhance it as needed!