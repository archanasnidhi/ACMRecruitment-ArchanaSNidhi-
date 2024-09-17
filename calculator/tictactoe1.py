import random

game_board = [' '] * 10
ai_marker = 'X'
player_marker = 'O'


def display_board(board):
    print('\n')
    print(f'{board[1]} | {board[2]} | {board[3]}')
    print('--|---|--')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print('--|---|--')
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print('\n')


def check_win():
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (7, 5, 3)
    ]
    for (a, b, c) in win_conditions:
        if game_board[a] == game_board[b] == game_board[c] and game_board[a] != ' ':
            return True
    return False


def check_draw():
    return ' ' not in game_board[1:]


def is_available(position):
    return game_board[position] == ' '


def place_marker(marker, position):
    if is_available(position):
        game_board[position] = marker

        if check_win():
            display_board(game_board)
            if marker == 'X':
                print("AI Wins!")
            else:
                print("Player Wins!")
            exit()

        if check_draw():
            display_board(game_board)
            print("It's a draw!")
            exit()
    else:
        print("Position already filled. Please try again")
        if marker == 'O':
            player_turn(marker)
        else:
            ai_turn(marker)


def player_turn(marker):
    while True:
        try:
            position = int(input("Enter the position to place your marker (1-9): "))
            if position < 1 or position > 9:
                print("Invalid option. Please try again")
            elif not is_available(position):
                print("Position already filled. Please try again")
            else:
                place_marker(marker, position)
                break
        except ValueError:
            print("Please enter a number between 1 and 9:")


def ai_turn(marker):
    position = random.randint(1, 9)
    while not is_available(position):
        position = random.randint(1, 9)
    place_marker(marker, position)


# Main game loop

while True:
    display_board(game_board)
    player_turn(player_marker)
    if check_win() or check_draw():
        break
    ai_turn(ai_marker)
    if check_win() or check_draw():
        break
