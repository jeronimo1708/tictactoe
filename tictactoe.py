# Creating the Board.

def display_board(board):
    
    print(' ' + board[7] + ' |' + ' ' + board[8] + ' |' + ' ' + board[9] + ' ')
    print('-----------')
    print(' ' + board[4] + ' |' + ' ' + board[5] + ' |' + ' ' + board[6] + ' ')
    print('-----------')
    print(' ' + board[1] + ' |' + ' ' + board[2] + ' |' + ' ' + board[3] + ' ')

# player decides if they want to be X or O. Function will save both player 1 and player 2 choices in the form of a tuple.
# This can be later retrieved.

def player_input():
    
    marker = ''
    
    while marker not in ['X','O']:
        marker = input('Player 1, Do you wanna be X or O ? : ').upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return('O','X')

# placing the marker at a position chosen by the player on the board.

def place_marker(board, marker, position):
    board[position] = marker

# win check against a mark( x and o)

def win_check(board, mark):
    
    return ((board[7] == board[8] == board[9] == mark) or # across the top
    (board[4] == board[5] == board[6] == mark) or # across the middle
    (board[1] == board[2] == board[3] == mark) or # across the bottom
    (board[7] == board[4] == board[1] == mark) or # down the middle
    (board[8] == board[5] == board[2] == mark) or # down the middle
    (board[9] == board[6] == board[3] == mark) or # down the right side
    (board[7] == board[5] == board[3] == mark) or # diagonal
    (board[9] == board[5] == board[1] == mark)) # diagonal

# to randomize the turns

import random

def choose_first():    
    flip = random.randint(0,1)    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):    
    return board[position] == ' '

def full_board_check(board):    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):    
    position = 0    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Please choose your next position (1 to 9):'))    
    return position

def replay():
    
    choice = ''
    
    while choice not in ['Y','N']:
        choice = input('Do you want to play again ? (Y or N) : ').upper()
        
    return choice == 'Y'

# setting the game logic

print('Welcome to Tic Tac Toe!')

while True:
    
    the_board = [' '] * 10
    
    player_1, player_2 = player_input()   # tuple unpacking
    
    who_goes_first = choose_first()       
    print(who_goes_first + ' goes first !')
    
    play_game = input('Do you want to play ? (Y or N) : '). upper()
    
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
        break
        
    while game_on == True:
        
        # player 1 turn
        
        if who_goes_first == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player_1,position)
            
            if win_check(the_board,player_1):
                display_board(the_board)
                print('Player 1 has won !')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is tied')
                    game_on = False
                    break
                else:
                    who_goes_first = 'Player 2'
                
        # player 2 turn
        
        else:
            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player_2,position)
            
            if win_check(the_board,player_2):
                display_board(the_board)
                print('Player 2 has won !')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is tied')
                    game_on = False
                    break
                else:
                    who_goes_first = 'Player 1'
                
                
    if not replay():
        break