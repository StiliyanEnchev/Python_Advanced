size = int(input())

matrix = []
alice_loc = []
tea_bags = 0
alice = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if 'A' in matrix[row]:
        alice = [row, matrix[row].index('A')]
        matrix[row][alice[1]] = '*'

while tea_bags < 10:
    command = input()

    row = alice[0] + directions[command][0]
    col = alice[1] + directions[command][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    alice = [row, col]
    element = matrix[row][col]
    matrix[row][col] = '*'

    if element == 'R':
        break

    if element.isdigit():
        tea_bags += int(element)

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print('She did it! She went to the party.')

[print(*row) for row in matrix]