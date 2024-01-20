rows, cols = [int(el) for el in input().split()]
matrix = [input().split() for _ in range(rows)]

equal_matrixes = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        symbol = matrix[row][col]

        if symbol == matrix[row][col+1] == matrix[row+1][col] == matrix[row+1][col+1]:
            equal_matrixes += 1

print(equal_matrixes)