size_of_the_mat = int(input())
matrix = [[x for x in input().split()] for row in range(size_of_the_mat)]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

max_eggs = float('-inf')
best_path = []
best_direction = ''
current_position = [[r, c] for r in range(size_of_the_mat) for c in range(size_of_the_mat) if matrix[r][c] == 'B']

for direction, position in directions.items():

    row = position[0] + current_position[0][0]
    col = position[1] + current_position[0][1]

    path = []
    collected_eggs = 0

    while 0 <= row < size_of_the_mat and 0 <= col < size_of_the_mat:

        if matrix[row][col] == 'X':
            break

        collected_eggs += int(matrix[row][col])
        path.append([row, col])

        row += position[0]
        col += position[1]

    if collected_eggs >= max_eggs:
        best_path = path
        best_direction = direction
        max_eggs = collected_eggs

print(best_direction)
print(*best_path, sep='\n')
print(collected_eggs)