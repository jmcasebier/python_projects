#!/usr/bin/env python3

# Tic-Tac-Toe Game in Python

# Initializing the board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Function to display the current board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Function to play the game
def play_game():
    display_board()
    while True:
        handle_turn("X")
        display_board()
        if check_for_win():
            print("X wins!")
            break
        elif check_for_tie():
            print("Tie!")
            break
        handle_turn("O")
        display_board()
        if check_for_win():
            print("O wins!")
            break
        elif check_for_tie():
            print("Tie!")
            break

# Function to handle a player's turn
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")
    board[position] = player

# Function to check for a win
def check_for_win():
    row_win = check_rows()
    col_win = check_columns()
    diag_win = check_diagonals()
    if row_win or col_win or diag_win:
        return True
    else:
        return False

# Function to check for a tie
def check_for_tie():
    if "-" not in board:
        return True
    else:
        return False

# Function to check rows for a win
def check_rows():
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        return True
    else:
        return False

# Function to check columns for a win
def check_columns():
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    if col_1 or col_2 or col_3:
        return True
    else:
        return False

# Function to check diagonals for a win
def check_diagonals():
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"
    if diag_1 or diag_2:
        return True
    else:
        return False

# Start game
play_game()

# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#         000  0000000000    000000000    #
#         000  00000000000  00000000      #
#         001  001 001 001  100           #
#         101  101 101 101  101           #
#         110  011 110 010  101           #
#         101  101  10 101  101           #
#         111  111   1 111  111           #
#    111  111  111     111  111           #
#    111 1 11  111     11    111 111 1    #
#     1 111     1      1      1 11 11     #
#                                         #
#          http://jmcasebier.com          #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #