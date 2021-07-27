# prints the display board
from IPython.display import clear_output

def display_board(board):
    # this works in jupyter only!
    # you can use "print('\n'*100)", to scroll up the previous board
    clear_output()

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    

# To select the marker
def select_marker_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

    
# places the marker at the desired position
def place_marker(board, marker, position):
    board[position] = marker

# returns True if there is win, else False
def win_check(board, mark):

    # across the top
    return((board[7] == mark and board[8] == mark and board[9] == mark) or
    # across the middle
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    # across the bottom
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    # down the left side
    (board[7] == mark and board[4] == mark and board[1] == mark) or
     # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    # down the right side
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    # leading diagonal
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    # trailing diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark))

import random

# random selection of first chance
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    
# checks for the availablity of slots on the board
def space_check(board, position):
    return board[position] == ' '

# returns True when board becomes full, else False
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# player makes a choice for placing the marker
def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        # if the particular slot is unavailble or
        #   invalid input index
        position = int(input('Choose your next position: (1-9) '))
    return position

def replay():
    pass
