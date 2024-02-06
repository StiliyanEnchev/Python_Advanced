class FullColumnError(Exception):
    pass


ROWS = 6
COLS = 7

DIRECTION_MAPPER = {
    'left': (0, -1),
    'up': (-1, 0),
    'main_diagonal': (-1, -1),
    'anti_diagonal': (-1, 1)
}

def print_board(board):
    for row in board:
        print(row)


def place_player_choice(col_index, player_num, board):

    for row_index in range(ROWS-1, -1, -1):
        if board[row_index][col_index] == 0:
            board[row_index][col_index] = player_num
            break
    else:
        raise FullColumnError('This column is full, please select another one')


def is_winner(board, current_col_inx, current_row_inx):
    for direction, coordinats in DIRECTION_MAPPER.items():
        pass

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

        place_player_choice(column_index, player, board)

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