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


# returns True for a new game, else False
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
    # Finally a while loop to combine the above functions
print('Welcome to Tic Tac Toe!')

while True:

    theBoard = [' '] * 10
    player1, player2 = select_marker_input()
    turn = choose_first()
    print(turn + ' gets to go first.')

    game = input('Are you ready to play? Enter Yes or No.')

    if game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    # Player1's turn.
    while game_on:
        if turn == 'Player 1':

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1, position)

            if win_check(theBoard, player1):
                display_board(theBoard)
                print('WELL DONE Player1! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a DRAW!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player 2's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2, position)

            if win_check(theBoard, player2):
                display_board(theBoard)
                print('CONGRATULATIONS Player 2!. You\'ve won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a DRAW!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break
