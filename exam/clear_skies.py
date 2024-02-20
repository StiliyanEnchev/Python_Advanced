size_of_airspace = int(input())


direction_mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

initial_armor_value = 300
current_location = []

airspace_matrix = []
all_enemies = 4
available_repairs = 0

for row in range(size_of_airspace):
    received_part = [str(x) for x in input()]
    airspace_matrix.append(received_part)

    if 'J' in received_part:
        current_location = [row, received_part.index('J')]

    if "R" in received_part:
        available_repairs += received_part.count('R')

while initial_armor_value > 0 and all_enemies > 0:

    command = input()

    current_row_loc, current_col_loc = current_location[0], current_location[1]
    next_row_loc = current_row_loc + direction_mapper[command][0]
    next_row_col = current_col_loc + direction_mapper[command][1]

    symbol = airspace_matrix[next_row_loc][next_row_col]
    current_location = [next_row_loc, next_row_col]
    airspace_matrix[current_row_loc][current_col_loc] = '-'
    airspace_matrix[next_row_loc][next_row_col] = 'J'

    if symbol == '-':
        continue

    elif symbol == 'E':
        if all_enemies > 1:
            all_enemies -= 1
            initial_armor_value -= 100
        else:
            all_enemies -= 1

    elif symbol == 'R':
        initial_armor_value = 300

if all_enemies == 0:
    print("Mission accomplished, you neutralized the aerial threat!")
elif initial_armor_value == 0:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates {current_location}!")

[print(''.join(row)) for row in airspace_matrix]
