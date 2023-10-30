import numpy as np


class Matrix:
    def __init__(self, n, m):
        self.rows = n
        self.cols = m
        self.matrix = np.zeros((self.rows, self.cols))

    def get(self, i, j):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            return self.matrix[i][j]
        else:
            return "Pozitia data nu exista in matrice"

    def set(self, i, j, value):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            self.matrix[i][j] = value
        else:
            return "Pozitia data nu exista in matrice"

    def transpose(self):
        return np.transpose(self.matrix)

    def multiply(self, other):
        if self.cols != len(other):
            raise ValueError("Matricile nu se pot inmulti")
        result = np.dot(self.matrix, other)
        return result

    def iterate(self, lambda_ftc):
        for i in range(self.rows):
            for j in range(self.cols):
                x = self.matrix[i][j]
                self.matrix[i][j] = lambda_ftc(x)
        return self.matrix


def double_lambda():
    return lambda x: x * 2


m = Matrix(2, 3)
m.set(0, 0, 1)
m.set(0, 1, 2)
m.set(0, 2, 3)
m.set(1, 0, 4)
m.set(1, 1, 5)
m.set(1, 2, 6)
print("Matricea initiala:")
print(m.matrix)

print("Transpose:")
print(m.transpose())

print("Matrix Multiplication:")
other_matrix = [
    [7, 4],
    [2, 1],
    [3, 5]
]
print(m.multiply(other_matrix))

print("2 x m:")
m.iterate(double_lambda())
print(m.matrix)
