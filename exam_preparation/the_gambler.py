n = int(input())


def print_board(board):
    for row in game_board:
        print(''.join(row))


game_board = []
gamblers_position = []
total_money = 100
jackpot_won = False

direction_mapper = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for current_row in range(n):
    received_row = list(input())
    game_board.append(received_row)

    if 'G' in received_row:
        gamblers_position = [current_row, received_row.index('G')]

direction = input()

while direction != 'end':
    try:
        game_board[gamblers_position[0]][gamblers_position[1]] = '-'

        row_direction, col_direction = direction_mapper[direction]
        new_position_row, new_position_col = gamblers_position[0] + row_direction, gamblers_position[1] + col_direction
        position_symbol = game_board[new_position_row][new_position_col]

        if position_symbol == 'W':
            total_money += 100

        elif position_symbol == 'P':
            total_money -= 200

        elif position_symbol == 'J':
            game_board[new_position_row][new_position_col] = 'G'
            gamblers_position = [new_position_row, new_position_col]
            total_money += 100000
            jackpot_won = True

            print(f"You win the Jackpot!\nEnd of the game. Total amount: {total_money}$")
            print_board(game_board)
            break

        game_board[new_position_row][new_position_col] = 'G'
        gamblers_position = [new_position_row, new_position_col]

        if total_money <= 0:
            print("Game over! You lost everything!")
            break

    except IndexError:
        print("Game over! You lost everything!")
        break

    direction = input()

if not jackpot_won and direction == 'end':
    print(f"End of the game. Total amount: {total_money}$")
    print_board(game_board)
