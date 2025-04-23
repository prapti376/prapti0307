class Matrix:
    def __init__(self, data):
        self.data = data

    def display(self):
        for row in self.data:
            print(row)

    def add(self, other):
        result = [[self.data[i][j] + other.data[i][j] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def multiply(self, other):
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
        return Matrix(result)

    def transpose(self):
        result = [[self.data[j][i] for j in range(3)] for i in range(3)]
        return Matrix(result)

# Example usage
m1 = Matrix([[1,2,3],[4,5,6],[7,8,9]])
m2 = Matrix([[9,8,7],[6,5,4],[3,2,1]])
m1.add(m2).display()
m1.multiply(m2).display()
m1.transpose().display()