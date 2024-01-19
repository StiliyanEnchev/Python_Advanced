matrix = []

row_num = int(input())

sum = 0

for index in range(row_num):
    matrix.append([int(x) for x in input().split()])
    sum += matrix[index][index]

print(sum)