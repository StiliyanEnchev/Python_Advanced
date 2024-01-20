num = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(num)]

primary_sum, secondary_num = 0, 0

for i in range(num):
    primary_sum += matrix[i][i]
    secondary_num += matrix[i][num - i - 1]

print(abs(primary_sum - secondary_num))