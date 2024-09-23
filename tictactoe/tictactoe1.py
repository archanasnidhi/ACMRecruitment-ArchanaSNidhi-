import random

board = [' '] * 10
c_marker = 'x'
h_marker = 'o'


def display(b):
    print(f'{b[1]} | {b[2]} | {b[3]}')
    print(f'{b[4]} | {b[5]} | {b[6]}')
    print(f'{b[7]} | {b[8]} | {b[9]}')
    print('-' * 10)


def win():
    conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
        (1, 5, 9), (7, 5, 3)              # Diagonals
    ]
    for condition in conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != ' ':
            return True
    return False


def draw():
    return board.count(' ') < 2


def available(pos):
    return board[pos] == ' '


def place(marker, pos):
    if available(pos):
        board[pos] = marker
        display(board)
        if win():
            print("Computer Wins!" if marker == c_marker else "Human Wins!")
            exit()
        if draw():
            print("It's a Draw!")
            exit()
    else:
        if marker == h_marker:
            pos = int(input("Not Free! Please re-enter a position: "))
        else:
            pos = random.randint(1, 9)
        place(marker, pos)


def human():
    pos = int(input("Enter the position to insert (1-9): "))
    place(h_marker, pos)


def computer():
    pos = random.randint(1, 9)
    place(c_marker, pos)


while not win():
    display(board)
    computer()
    human()
