#########################################################################################
#
#                                       Neural Network
#   Joshua Pickard                                                          June 2020
#   jpic@umich.edu
#
#   Purpose: This class defines a simple feed forward neural network with the goal of 
#            controlling a snake object.
#
#   Network Structure: The network will have an input layer of 32, 2 hidden layer of 16
#                      neurons each, and 1 output layer of 4 neurons.
#       Input layer: The snake will have "vision" in 8 directions. In each direction, 
#                    it will see 3 things: 
#                       1. distance to the wall
#                       2. if food is in that direction
#                       3. distance to itself
#                    Additionally, there will be 4 inputs for the 
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
#       - __init__.......initializes a network with random values
#       - __init__.......initializes a network with values written in a text file
#       - feed_forward...conducts a series of matrix multiplications and activation
#                        functions (currently the sigmoid function) to produce an output
#                        vector
#       - activate.......applies the sigmoid function to every element in a vector
#       - sigmoid........1/(1+e^-x)
#       - print..........used to write the network to a file
#
#########################################################################################
import numpy as np
import os
import math
import sys

class Cneural_net:

    #####################################################################################
    #
    #   Cneural_net:__init__
    #       Parameters: 1. p_directory_path...the path of the file storing the values to 
    #                                         initialize the netork. If it is "new",
    #                                         then it is randomly initialized.
    # 
    #       Description: Initializes weights and basis matrices
    #
    #####################################################################################
    def __init__(self, p_directory_path):
        self.W = {}
        self.B = {}
        if p_directory_path != "new":
            self.W[1] = np.loadtxt(p_directory_path + "/W_1", delimiter=' ')
            self.W[2] = np.loadtxt(p_directory_path + "/W_2", delimiter=' ')
            self.W[3] = np.loadtxt(p_directory_path + "/W_3", delimiter=' ')
            self.B[1] = np.loadtxt(p_directory_path + "/B_1", delimiter=' ')
            self.B[2] = np.loadtxt(p_directory_path + "/B_2", delimiter=' ')
            self.B[3] = np.loadtxt(p_directory_path + "/B_3", delimiter=' ')
        else:
            self.W[1] = np.random.randn(16, 32).round(decimals=7)
            self.W[2] = np.random.randn(16, 16).round(decimals=7)
            self.W[3] = np.random.randn(4, 16).round(decimals=7)
            self.B[1] = np.random.randn(16, 1).round(decimals=7)
            self.B[2] = np.random.randn(16, 1).round(decimals=7)
            self.B[3] = np.random.randn(4, 1).round(decimals=7)  
                  

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
    def activate(self, p_vector):
        return self.sigmoid(p_vector)

    #####################################################################################
    #
    #   Cneural_net:sigmoid
    #       Parameters: 1. x...the input to the function
    #
    #       Return: 1/(1+e^-x) 
    #
    #####################################################################################
    def sigmoid(self, p_x):
        return 1/(1+math.e^(-p_x))

    #####################################################################################
    #
    #   Cneural_net:print
    #       Parameters: 1. p_directory_path...the directory to store the network data
    #
    #       Return: prints weights and basis matrices to the text file in file_path
    #
    #####################################################################################
    def print(self, p_directory_path):
        os.mkdir(p_directory_path)
        origional_output = sys.stdout
        #sys.stdout = open(p_file_path, "w")
        for i in self.W:
            sys.stdout = open(p_directory_path + "/W_" + str(i), "w")
            np.savetxt(p_directory_path + "/W_" + str(i), self.W[i], fmt="%.7f")
            #print(self.W[i])
        for i in self.B:
            sys.stdout = open(p_directory_path + "/B_" + str(i), "w")
            np.savetxt(p_directory_path + "/B_" + str(i), self.B[i], fmt="%.7f")
            #print(self.B[i])
        sys.stdout = origional_output
    
    