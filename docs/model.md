# Looi Model

The `model.py` script provided here defines the architecture of the neural network model used for training and inference in the chatbot application. This README explains the model architecture, the thought process behind it, its usage, the packages utilized, and the functions involved, along with customization options.

## Model Architecture

The neural network model implemented here is a simple feedforward neural network with three fully connected layers (also known as linear layers) and ReLU activation functions between them. The model architecture can be summarized as follows:

1. **Input Layer (`input_size`):**
   - The input layer consists of neurons equal to the size of the input feature vector, representing the bag of words representation of the input text.

2. **Hidden Layers (`hidden_size`):**
   - Two hidden layers are included, each with the same size specified by the `hidden_size` parameter.
   - ReLU (Rectified Linear Unit) activation functions are applied after each hidden layer to introduce non-linearity into the model.

3. **Output Layer (`num_classes`):**
   - The output layer consists of neurons equal to the number of classes or categories in the classification task.
   - No activation function is applied to the output layer, allowing for raw scores to be generated for each class.

## Thought Process

- **Simplicity:** A simple feedforward neural network architecture is chosen for its ease of implementation and understanding.
- **Non-Linearity:** ReLU activation functions are used to introduce non-linearity and increase the model's capacity to learn complex patterns in the data.
- **Scalability:** The model architecture can be easily scaled by adjusting the size of the hidden layers or adding more layers for increased complexity if needed.

## Usage

1. **Model Definition:**
   - Import the `NeuralNet` class from `model.py` into the training script (`train.py`) and instantiate the model with appropriate input, hidden, and output sizes.

2. **Forward Pass:**
   - Pass input data through the model using the `forward()` method to obtain predictions or output scores for each class.

3. **Training and Inference:**
   - Train the model using labeled data and optimize its parameters to minimize the loss.
   - Use the trained model for inference by passing input data through it to make predictions.

## Packages Used

- **torch**: PyTorch library for building and training neural networks.
- **torch.nn**: PyTorch's neural network module for defining neural network layers and architectures.

## Functions

- **NeuralNet**: Class definition for the neural network model, including the initialization of layers and the forward pass method.

## Customization

- **Model Architecture**: Experiment with different architectures by adjusting the number of hidden layers, their sizes, or adding additional layers.
- **Activation Functions**: Explore alternative activation functions such as sigmoid or tanh to introduce different non-linearities.
- **Regularization**: Add dropout layers or apply weight regularization techniques to prevent overfitting and improve generalization.
---

This README provides detailed information about the chatbot model architecture, its implementation, usage, customization options, and potential contributions. Feel free to further enhance it as needed!