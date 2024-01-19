n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(input()))

symbol = input()
found = False

for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{symbol} does not occur in the matrix")
