import random
import math

class Matrix:
    def __init__(self, data):
        self.num_rows = len(data)
        self.num_cols = len(data[0])
        self.data = data

    @classmethod
    def generate_random(cls, num_rows: int, num_cols: int):
        data = [[random.uniform(-1, 1) for _ in range(num_cols)] for _ in range(num_rows)]
        return cls(data)
    
    @classmethod
    def generate_from_row(cls, row):
        return cls([row])
    
    def __mul__(self, other):
        if self.num_cols != other.num_rows:
            raise Exception(f"Mismatched order of Matrices for multiplication {(self.num_rows, self.num_cols)} vs {(other.num_rows, other.num_cols)}")
        
        result = [[0 for _ in range(other.num_cols)] for _ in range(self.num_rows)]
        
        for i in range(self.num_rows):
            for j in range(other.num_cols):
                for k in range(self.num_cols):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        
        return Matrix(result)
    
    def __add__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise Exception(f"Mismatched order of Matrices for addition {(self.num_rows, self.num_cols)} vs {(other.num_rows, other.num_cols)}")
        
        result = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                result[i][j] = self.data[i][j] + other.data[i][j]
        
        return Matrix(result)
    
    # Sigmoid activation function to a matrix
    def sigmoid(self):
        if self.num_rows != 1:
            raise Exception("Can't apply activation function for non row matrix")
        
        for i in range(self.num_cols):
            self.data[0][i] = 1 / (1 + math.e ** -self.data[0][i])

    def mutate(self, fuzz_factor: float):
        for row in self.data:
            for i in range(len(row)):
                row[i] += random.uniform(-fuzz_factor, fuzz_factor)
                row[i] *= 1 + random.uniform(-fuzz_factor, fuzz_factor)

class NeuralNetwork:
    def __init__(self, architecture):
        self.architecture = architecture
        self.layers = [] 
        self.biases = [] 

        # Initialize layers and biases based on the architecture
        for i in range(len(architecture) - 1):
            self.layers.append(Matrix.generate_random(architecture[i], architecture[i + 1]))
            self.biases.append(Matrix.generate_random(1, architecture[i + 1]))

    # Solve for output
    def solve(self, input_matrix: Matrix) -> Matrix:
        temp = input_matrix
        
        for layer, bias in zip(self.layers, self.biases):
            temp = temp * layer 
            temp = temp + bias 
            temp.sigmoid()
        
        return temp
    
    def mutate(self, fuzz_factor: float):
        for layer in self.layers:
            layer.mutate(fuzz_factor)
        for bias in self.biases:
            bias.mutate(fuzz_factor)

    # Convert the neural network object to a string representation
    def __str__(self):
        result = (f"Architecture: {self.architecture} | ")
        
        for i, layer in enumerate(self.layers):
            result += (f"Layer #{i}: {layer.data}, ")
        
        result = result[:-1]
        result += ("| ")
        
        for i, bias in enumerate(self.biases):
            result += (f"Bias #{i}: {bias.data}, ")
        
        return result[:-2]
    
    def crossover(self, other):
        for i in range(len(self.layers)):
            for j in range(len(self.layers[i].data)):
                for k in range(len(self.layers[i].data[j])):
                    if random.random() < 0.5:
                        self.layers[i].data[j][k] = other.layers[i].data[j][k]
        for i in range(len(self.biases)):
            for j in range(len(self.biases[i].data)):
                for k in range(len(self.biases[i].data[j])):
                    if random.random() < 0.5:
                        self.biases[i].data[j][k] = other.biases[i].data[j][k]