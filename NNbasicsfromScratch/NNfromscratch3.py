import numpy as np
import random

np.random.seed(0)

X = [[1, 2, 3, 2.5],
    [2.0, 5.0, -1.0, 2.0],
    [-1.5, 2.7, 3.3, -0.8]]

"""
// Implemeting ReLu activation manually

inputs = [0, 2,  3.3, -2.7, 1.1, 2.2, -100]
outputs=[]

for i in inputs:
    outputs.append(max(i,0))
print(outputs)
"""
# Creating Toy dataset
def spiral_data(points, classes):
    X = np.zeros((points*classes, 2))
    y = np.zeros(points*classes, dtype='uint8')
    for class_number in range(classes):
        ix = range(points*class_number, points*(class_number+1))
        r = np.linspace(0.0, 1, points)  # radius
        t = np.linspace(class_number*4, (class_number+1)*4, points) + np.random.randn(points)*0.2
        X[ix] = np.c_[r*np.sin(t*2.5), r*np.cos(t*2.5)]
        y[ix] = class_number
    return X, y

## Lading the data
X,y = spiral_data(100, 3)

#Creating Layer and Activation function(ReLu)
class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))  

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLu:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)




layer1 = Layer_Dense(2,5)
activation1 = Activation_ReLu()

layer1.forward(X)
activation1.forward(layer1.output)

#print(layer1.output)
print(activation1.output)


















