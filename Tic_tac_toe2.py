{\rtf1\ansi\ansicpg1252\cocoartf2511
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww13960\viewh11940\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \
\
\
import IPython\
IPython.__version__\
\
from IPython.display import clear_output\
\
def display_board(board):\
    \
    print(board[7]+ '|' + board[8]+ '|' + board[9])\
    print(board[4]+ '|' + board[5]+ '|' + board[6])\
    print(board[1]+ '|' + board[2]+ '|' + board[3])\
    \
\
\
test_board = ['#','X','O','X','O','X','O','X','O','X']\
display_board(test_board)\
\
\
def player_input():\
    \
    marker = ''\
    \
    while marker != 'X' and marker!='O':\
        marker = input(' Player 1, choose X or O:').upper()\
    \
    player1 = marker\
    \
    if player1 == 'X':\
            player2 = 'O'\
            \
    else:\
        player2 ='X'\
    \
    return(player1, player2)\
        \
\
playe1_marker, player2_marker = player_input() \
\
\
def place_marker (board, marker, position):\
   board[position] = marker \
\
\
place_marker(test_board, '$',8)\
display_board(test_board)\
\
\
\
def win_check(board, mark):\
    # WIN TIC TRAC TOE?\
    # ALL ROWS, AND CHECK TO SEE IF THEY ALL SHARE THE SAME MARKER?\
     return ((board[1]== board[2]== board[3]== mark) or \
        (board[4]== board[5]== board[6] == mark) or \
        (board[7]== board[8]== board[9] == mark) or\
    \
    # ALL COLUMNS, ALSO\
         (board[1]==  board[4]==  board[7]== mark) or\
         (board[2]==  board[5]==  board[8] == mark) or\
         (board[3]==  board[6]==  board[9] == mark) or\
    # TWO DIAGONALS\
    (board[1]==  board[5]==  board[9]== mark) or\
    (board[3]==  board[5]==  board[7]== mark))\
\
\
\
display_board(test_board)\
\
\
win_check(test_board, 'O')\
\
\
import random\
\
def choose_first():\
    \
    flip = random.randint(0,1)\
    \
    if flip == 0:\
        return 'Player 1'\
    else:\
        return 'Player 2'\
\
\
\
choose_first()\
\
\
def space_check(board, position):\
    return board[position] == ' '\
\
\
\
def full_board_check(board):\
    for i in range(1,10):\
        if space_check(board,i):\
            return False\
        # BOARD IS FULL IF WE RETURN TRUE\
    \
    return True\
\
\
\
\
def player_choice(board):\
    \
    position = 0\
    \
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):\
        position = int (input('Choose a position: (1-9)'))\
        \
        return position\
\
\
\
\
def replay():\
    choice= input('Play again? Enter Yes or No')\
    \
    return choice == 'Yes'\
\
\
#WHILE LOOP TO KEEP RUNNING THE GAME\
\
print('Welcome to Tic Tac Toe')\
\
while True:\
    \
    #Play the game\
    \
    # set everything up(board, whis first, choose markers)\
    \
    the_board = [' ']*10\
    player1_marker, player2_marker = player_input()\
    \
    turn = choose_first()\
    print(turn + ' will go first')\
    \
    play_game = input ('Ready to play? y or n?')\
    \
    if play_game == 'y':\
        game_on = True\
    else: \
        game_on = False\
        \
    \
    # game play\
    \
    while game_on:\
        \
        if turn == 'Player 1':\
            \
            # show the board\
            \
            display_board(the_board)\
            \
            # choose a position\
            position = player_choice(the_board)\
            \
            \
            # place the marker on position chosen\
            place_marker(the_board, player1_marker,position)\
            \
            # check if they won\
            if win_check(the_board, player1_marker):\
                    display_board(the_board)\
                    print('Player 1 has won!!')\
                    game_on = False\
                    \
            else:\
                    if full_board_check(the_board):\
                        display_board(the_board)\
                        print('Tie Game!!')\
                        game_on = False\
                    else:\
                        turn = 'Player 2'\
                        \
                        \
        else:\
            \
            # show the board\
            \
            display_board(the_board)\
            \
            # choose a position\
            position = player_choice(the_board)\
            \
            \
            # place the marker on position chosen\
            place_marker(the_board, player2_marker,position)\
            \
            # check if they won\
            if win_check(the_board, player2_marker):\
                    display_board(the_board)\
                    print('Player 2 has won!!')\
                    game_on = False\
            \
            # or check if there is a tie\
            else:\
                    if full_board_check(the_board):\
                        display_board(the_board)\
                        print('Tie Game!!')\
                        game_on = False\
                    else:\
                        turn = 'Player 1'\
                    \
    \
    if not replay():\
            break\
# BREAK OUT OF THE WHILE LOOP ON replay()\
\
\
\
\
\
\
\
\
\
\
\
}