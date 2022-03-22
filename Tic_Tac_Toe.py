# The Interactive Tic-Tac-Toe Game 

# 3*3 board display for the players
def display_board(board):
    print("-------------")
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print("-------------")
    print("|",board[3],"|",board[4],"|",board[5],"|")
    print("-------------")
    print("|",board[6],"|",board[7],"|",board[8],"|")
    print("-------------")
    

# Get the marker input from the first player    
def player_input():
    marker = ''
    symbol='WRONG'
    valid_symbols = ['X','O','x','o']
    symbol = input('Player 1: Do you want to be X or O? ')
    while symbol not in valid_symbols:
        symbol = input('Wrong input!! Player 1 please input a valid symbol (X or O): ')    
    marker = symbol.upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
# Defining the player marker on the 3*3 board
def place_marker(board, marker, position):
    if (position == 1):board[0] = marker
    if (position == 2):board[1] = marker
    if (position == 3):board[2] = marker
    if (position == 4):board[3] = marker
    if (position == 5):board[4] = marker
    if (position == 6):board[5] = marker
    if (position == 7):board[6] = marker
    if (position == 8):board[7] = marker
    if (position == 9):board[8] = marker

        
        
#Checking whether the last marked player has won or not
def win_check(board, marker):
    if (marker == 'X'):
        if ( board[0] == board[1] == board[2] == 'X' or 
             board[3] == board[4] == board[5] == 'X' or
             board[6] == board[7] == board[8] == 'X' or
             board[0] == board[3] == board[6] == 'X' or
             board[1] == board[4] == board[7] == 'X' or
             board[2] == board[5] == board[8] == 'X' or
             board[0] == board[4] == board[8] == 'X' or
             board[2] == board[4] == board[6] == 'X'):
            print("Player 'X' has won this game. Congrats!!")
            return True    
    if (marker == 'O'):
        if ( board[0] == board[1] == board[2] == 'O' or 
             board[3] == board[4] == board[5] == 'O' or
             board[6] == board[7] == board[8] == 'O' or
             board[0] == board[3] == board[6] == 'O' or
             board[1] == board[4] == board[7] == 'O' or
             board[2] == board[5] == board[8] == 'O' or
             board[0] == board[4] == board[8] == 'O' or
             board[2] == board[4] == board[6] == 'O'):
            print("Player 'O' has won this game. Congrats!!")
            return True
    else:
            return False
        
        
        
#Chose the first player randomly
def choose_first():
    player = int(random.randint(1,2))
    if  (player == 1):
        return "Player 1"
        
    elif (player == 2):
        return "Player 2"
    
    
    
#Check whether the chosen position is already marked or not    
def space_check(board, position):
    if (board[position-1] == ' ' ):
        return True
    else:
        return False
    
    
    
#Check whether the board is fully marked or not    
def full_board_check(board):
    for box in board:
        if box == ' ':
            return False
    Print("This game is a Tie, Nobody won!!")
    return True


#Get the next postion input from the player 
def player_choice(board):
    position_range = ['1','2','3','4','5','6','7','8','9']
    position = input('Enter your next position of choice between 1 and 9: ')
    while position not in position_range or  space_check(board, int(position)) == False:
            print('The chosen position is either already occupied or wrong!!')
            position = input('Please input an available valid postion number between 1 and 9: ')
    
    return int(position)


#Checking whether the player want to replay the game or not
def replay():
    replay_msg_list=['Y','N','n','y']
    replay_msg= input('Do you want to play (Y/N): ')
    while replay_msg not in replay_msg_list:
        print('That is not a valid input!!')
        replay_msg=input("Please provide 'Y' for GAME CONTINUE and 'N' for GAME EXIT:  ")
    if replay_msg.upper() == 'Y':
        return True
    elif replay_msg.upper() == 'N':
        return False
    
    

#The game play

from IPython.display import clear_output
import random
while True:
    print('Welcome to the tic-tac-toe game! Have fun!')
    print('Please note all the positions you can choose from the board while playing')
    win_flag = full_board_flag = False
    position = 0
    board = ['1','2','3','4','5','6','7','8','9']
    display_board(board)
    print("Okay, Let's begin")
    print("We have the empty board now")
    board = [' ']*9
    display_board(board) 
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
        player1_marker,player2_marker = player_input()
        print(f'Player 1 marker : {player1_marker} ')
        print(f'Player 2 marker : {player2_marker} ')
        player_turn=choose_first()
        print(f'{player_turn} can start first')
    else:
        game_on = False
    
  
    while game_on:
        
        if  player_turn == 'Player 1':
            position=player_choice(board)
            place_marker(board, player1_marker, position)
            display_board(board)
            win_flag=win_check(board, player1_marker)
            if win_flag == True:
                game_on = False
                full_board_flag = full_board_check(board)
            else:
                if full_board_flag == True:
                    display_board(board)
                    break
                else:
                    player_turn = 'Player 2'
            
            
        if  player_turn == 'Player 2':
            position=player_choice(board)
            place_marker(board, player2_marker, position)
            display_board(board)
            win_flag=win_check(board, player2_marker)
            if win_flag == True:
                game_on = False
                full_board_flag = full_board_check(board)
            else:
                if full_board_flag == True:
                    display_board(board)
                    break
                else:
                    player_turn = 'Player 1'
            
                        
    if (replay()):
        continue         
    else:
        break
             
