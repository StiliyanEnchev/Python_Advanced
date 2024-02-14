def is_in_scope(row_index, col_index, row_count, col_count):
    return 0 <= row_index < row_count and 0 <= col_index < col_count


n, m = [int(el) for el in input().split()]

neighborhood = []
boy_starting_loc = None

direction_mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for current_row in range(n):
    received_data = list(input())
    neighborhood.append(received_data)

    if 'B' in received_data:
        boy_starting_loc = (current_row, received_data.index('B'))

current_position = boy_starting_loc

while True:
    direction = input()

    current_row, current_col = current_position
    row_movement, col_movement = direction_mapper[direction]
    next_row = current_row + row_movement
    next_col = current_col + col_movement

    if not is_in_scope(next_row, next_col, n, m):
        neighborhood[boy_starting_loc[0]][boy_starting_loc[1]] = ' '
        print("The delivery is late. Order is canceled.")
        break

    symbol = neighborhood[next_row][next_col]

    if symbol == '*':
        continue

    current_position = [next_row, next_col]

    if symbol == 'P':
        print("Pizza is collected. 10 minutes for delivery.")
        neighborhood[next_row][next_col] = 'R'

    elif symbol == 'A':
        neighborhood[next_row][next_col] = 'P'
        print("Pizza is delivered on time! Next order...")
        break

    elif symbol == '-':
        neighborhood[next_row][next_col] = '.'


for row in neighborhood:
    print(''.join(row))
