size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

command = input().split()

while command[0] != 'END':
    action, r, c, num = command[0], int(command[1]), int(command[2]), int(command[3])

    if not (0 <= r < size and 0 <= c < size):
        print("Invalid coordinates")
    elif action == 'Add':
        matrix[r][c] += num
    elif action == 'Subtract':
        matrix[r][c] -= num

    command = input().split()

[print(*row) for row in matrix]
