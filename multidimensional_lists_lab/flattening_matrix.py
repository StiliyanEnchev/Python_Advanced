row = int(input())
matrix = []

for _ in range(row):
    data = [int(x) for x in input().split(', ')]
    matrix.extend(data)

print(matrix)