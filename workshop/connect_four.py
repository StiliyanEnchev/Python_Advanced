class FullColumnError(Exception):
    pass


ROWS = 6
COLS = 7

DIRECTION_MAPPER = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0),
    'up_left': (-1, -1),
    'down_right': (1, 1),
    'up_right': (-1, 1),
    'down_left': (1, -1)
}

def print_board(board):
    for row in board:
        print(row)


def place_player_choice(col_index, player_num, board):

    for row_index in range(ROWS-1, -1, -1):
        if board[row_index][col_index] == 0:
            board[row_index][col_index] = player_num
            return [row_index, col_index]
    else:
        raise FullColumnError('This column is full, please select another one')


def is_winner(board, current_loc, player):

    current_row, current_col = current_loc[0], current_loc[1]
    counter = 1
    searched_element = board[current_row][current_col]

    for coordinates in DIRECTION_MAPPER.values():
        next_row, next_col = coordinates

        while board[current_row + next_row][current_col + next_col] == searched_element:
            counter += 1

            if counter == 4:
                return('Yes')

  


board = []

for _ in range(ROWS):
    board.append([0 for _ in range(COLS)])

turns = 1

while True:
    player = 2 if turns % 2 == 0 else 1

    try:
        column = input(f'Player {player}, please choose a column: ')
        column_index = int(column) - 1

        if column_index < 0:
            print('The number must be positive and different than zero.')
            continue

        current_loc = place_player_choice(column_index, player, board)

        is_winner(board, current_loc, player)

    except FullColumnError:
        print("This column is full, please select another one")
        continue
    except IndexError:
        print('This column is invalid, please select another one')
        continue
    except ValueError:
        print('Please select a number')
        continue

    print_board(board)
    turns += 1

print(f'And the winner is player {player}')
print_board(board)