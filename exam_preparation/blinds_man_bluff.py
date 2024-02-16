number_of_rows, number_of_cols = [int(x) for x in input().split()]


def is_in_scope(playground, next_row, next_col, number_of_rows, number_of_cols):

    if 0 <= next_row < number_of_rows and 0 <= next_col < number_of_cols:
        return playground[next_dir_row][next_dir_col]



playground = []
player_location = []
players_found = 0
moves_counter = 0

direction_mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(number_of_rows):
    current_row = input().split()
    playground.append(current_row)

    if 'B' in current_row:
        player_location = [row, current_row.index('B')]


while players_found != 3:
    command = input()

    if command == 'Finish':
        break

    next_dir_row = player_location[0] + direction_mapper[command][0]
    next_dir_col = player_location[1] + direction_mapper[command][1]

    if is_in_scope(playground, next_dir_row, next_dir_col, number_of_rows, number_of_cols):
        symbol = playground[next_dir_row][next_dir_col]
    else:
        continue

    if symbol == 'O':
        continue

    elif symbol == '-':
        player_location = [next_dir_row, next_dir_col]

    elif symbol == 'P':
        players_found += 1

    playground[player_location[0]][player_location[1]] = '-'
    playground[next_dir_row][next_dir_col] = 'B'
    player_location = [next_dir_row, next_dir_col]
    moves_counter += 1

print(f"Game over!\nTouched opponents: {players_found} Moves made: {moves_counter}")