#########################################################################################
#
#                                       Neural Network
#   Joshua Pickard                                                          June 2020
#   jpic@umich.edu
#
#   Purpose: This class defines a simple feed forward neural network with the goal of 
#            controlling a snake object.
#
#   Network Structure:  The network will have an input layer of 32, 2 hidden layer of 16
#                       neurons each, and 1 output layer of 4 neurons.
#       Input layer: The snake will have "vision" in 8 directions. In each direction, 
#                    it will see 3 things: the distance to the wall, the distance to food, and the
#                    distance to itself. Additionally, there will be 4 inputs for the 
#                    head and tail respectively, indicating the direction they are 
#                    moving. (8*3+2*4=32)
#       Output layer: The network will have an output layer with 4 nodes, each 
#                     corresponding to an input a human player could enter to control
#                     the snake.
#       
#
#   Class attributes:
#       1. W...a dictionary storing the weight matrices
#       2. B...a dictionary storing the bias matrices
#
#   Methods:
#       - __init__.......accepts a list defining layer list and initializes weight_list
#                        and bias_list with appropriatly sized matrices of random values
#       - feed_forward...conducts a series of matrix multiplications and activation
#                        functions (currently the sigmoid function) to produce an output
#                        vector
#       - activate.......applies the sigmoid function to every element in a vector
#       - sigmoid........1/(1+e^-x)
#
#########################################################################################
import numpy as np
import math

class Cneural_net:

    #####################################################################################
    #
    #   Cneural_net:__init__
    #       Description: Initializes weights and basis matrices
    #
    #####################################################################################
    def __init__(self):
        self.W = {}
        self.B = {}
        self.W[1] = np.random.randn(16, 32)
        self.W[2] = np.random.randn(16, 16)
        self.W[3] = np.random.randn(4, 16)
        self.B[1] = np.random.randn(16, 31)
        self.B[2] = np.random.randn(16, 1)
        self.B[3] = np.random.randn(4, 1)


    #####################################################################################
    #
    #   Cneural_net:feed_forward
    #       Parameters: 1. p_input_vector...defines the values of the first layer of the
    #                                       network
    #
    #       Description: Iterates a series of matrix multiplications and acitvation 
    #                    functions to produce an output vector. 
    #
    #####################################################################################
    def feed_forward(self, p_input_vector):
        layer_1 = self.activate(np.matmul(W[1],p_input_vector)+B[1])
        layer_2 = self.activate(np.matmul(W[2],layer_1)+B[2])
        output = self.activate(np.matmul(W[3],layer_2)+B[3])
        return output

    #####################################################################################
    #
    #   Cneural_net:activate
    #       Parameters: 1. vector...the input vector to the function
    #
    #       Return: a vector where the sigmoid function has been applied to each element in x 
    #
    #       Note: This function exist as a means of making it simple to change which 
    #             activation function is being used (i.e. relu, tanh) without modifying 
    #             the feed_forward method
    #
    #####################################################################################
    def activate(self, vector):
        retrun self.sigmoid(vector)

    #####################################################################################
    #
    #   Cneural_net:sigmoid
    #       Parameters: 1. x...the input to the function
    #
    #       Return: 1/(1+e^-x) 
    #
    #####################################################################################
    def sigmoid(self, x):
        return 1/(1+math.e^(-x))







"""
        self.W1 = 
        self.W2 = 
        self.W3 = 
        self.B1 = 
        self.B2 = 
        self.B3 = 
"""


"""
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.colors
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, mean_squared_error
    from tqdm import tqdm_notebook

    from sklearn.preprocessing import OneHotEncoder
    from sklearn.datasets import make_blobs

    #creating my own color map for better visualization
    my_cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["red","yellow","green"])

    #Generating 1000 observations with 4 labels - multi class
    data, labels = make_blobs(n_samples=1000, centers=4, n_features=2, random_state=0)
    print(data.shape, labels.shape)

    #visualize the data
    plt.scatter(data[:,0], data[:,1], c=labels, cmap=my_cmap)
    plt.show()

    #converting the multi-class to binary 
    labels_orig = labels
    labels = np.mod(labels_orig, 2)
    plt.scatter(data[:,0], data[:,1], c=labels, cmap=my_cmap)
    plt.show()

    #split the binary data
    X_train, X_val, Y_train, Y_val = train_test_split(data, labels, stratify=labels, random_state=0)
    print(X_train.shape, X_val.shape)
"""