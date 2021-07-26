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

def win_check(board, mark):
    pass
    
import random

def choose_first():
    pass

def space_check(board, position):
    pass

def full_board_check(board):
    pass

def player_choice(board):
    pass

def replay():
    pass
