class Matrix:
    def __init__(self, data):
        if len(data) != 3 or any(len(row) != 3 for row in data):
            raise ValueError("Only 3x3 matrices are supported.")
        self.data = data

    def display(self):
        for row in self.data:
            print(row)

    def __add__(self, other):
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(3)]
            for i in range(3)
        ]
        return Matrix(result)

    def __matmul__(self, other):  
        result = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    def transpose(self):
        result = [
            [self.data[j][i] for j in range(3)]
            for i in range(3)
        ]
        return Matrix(result)


matrix1 = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrix2 = Matrix([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

print("Matrix 1:")
matrix1.display()

print("\nMatrix 2:")
matrix2.display()


print("\nMatrix Addition (Matrix1 + Matrix2):")
add_result = matrix1 + matrix2
add_result.display()


print("\nMatrix Multiplication (Matrix1 * Matrix2):")
mul_result = matrix1 @ matrix2
mul_result.display()

print("\nTranspose of Matrix 1:")
trans_result = matrix1.transpose()
trans_result.display()
