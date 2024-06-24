# Neural Networks

- Neurons are connected to and receive electrical signals from other neurons.
- Neurons process input signals and can be activated.

**Artificial Neural Networks**
- Model mathematical function from inputs to outputs based on the structure and parameters of the network.
- Allows for learning the network's parameters based on data.

**logistic sigmoid**
g(x) = e<sup>x</sup>/e<sup>x</sup>+1

**rectified linear unit(ReLU)**
g(x) = max(0, x)

**gradient descent**
algorithm for minimizing loss when training neural network

**Stochastic Gradient Descent**
- Start with a random choice of weights.
- Repeat:
    - Calculate the gradient based on one data point:
      direction that will lead to decreasing loss.
    - Update weights according to the gradient.

**Mini-Batch Gradient Descent**
- Start with a random choice of weights.
- Repeat:
    - Calculate the gradient based on one small batch:
      direction that will lead to decreasing loss.
    - Update weights according to the gradient.

**Gradient Descent**
- Start with a random choice of weights.
- Repeat:
    - Calculate the gradient based on all data points:
      direction that will lead to decreasing loss.
    - Update weights according to the gradient.

**Perceptron**
- Only capable of learning linearly separable decision boundary.

**multilayer neural network**
artificial neural network with an input layer, an output layer, and at least one hidden layer

**back propagation**
algorithm for training neural networks with hidden layers

- start with a random choice of weights.
- Repeat:
   - Calculate error for output layer.
   - For each layer, starting with output layer, and moving inwards towards earliest hidden layer:
       - Propagate error back one layer.
       - Update weights.

**deep neural networks**
neural network with multiple hidden layers

**dropout**
temporarily removing units - selected at random - from a neural network to prevent over-reliance on certain units

**pooling**
reducing the size of an input by sampling from regions in the input

**ma-pooling**
pooling by choosing the maximum value in each region

**convolutional neural network**
neural networks that use convolution, usually for analyzing images

**feed_forward neural network**
neural network that has connections only in one direction