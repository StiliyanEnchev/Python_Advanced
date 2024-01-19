row, col = [int(x) for x in input().split(', ')]

matrix = []
total_sum = 0

for i in range(row):
    data = [int(el) for el in input().split(', ')]
    matrix.append(data)
    total_sum += sum(data)

print(total_sum)
print(matrix)