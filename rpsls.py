#!/usr/bin/env python3

#imports
from random import randint
from os import system, name

#clear screen
def clear():
    if name == 'posix':
        _ = system('clear')
    else:
        _ = system('clr')

#begin the game
def beginGame():
    clear()
    #introduce game
    print('Welcome to Rock-Paper-Scissors-Lizard-Spock!')
    show_moves()
    get_moves()

#present option to play again
def gameOver():
    playAgain = input('\nPlay again? (y or n): ')
    #verify yes or no response
    yesOrNo = ('y', 'n', 'yes', 'no')
    while playAgain.lower() not in yesOrNo:
        playAgain = input('\nPlease enter y to play again or n to exit: ')

    #respond to user selection
    if playAgain.lower() == 'y' or playAgain.lower() == 'yes':
        beginGame()
    else:
        clear()
        exit()

#introduce all possible moves
def show_moves():
    print('\n1 - Rock\n2 - Paper\n3 - Scissors\n4 - Lizard\n5 - Spock\n')

#prompt user for move selection
def get_moves():
    user_move = input('Make your selection: ')
    #verify user selection validity
    moves = ('1', '2', '3', '4', '5')
    while user_move not in moves:
        user_move = input('\nPlease enter the number of your selection: ')

    #generate computer selection
    comp_move = str(randint(1, 5))
    if comp_move == '1':
        comp = 'Rock'
    elif comp_move == '2':
        comp = 'Paper'
    elif comp_move == '3':
        comp = 'Scissors'
    elif comp_move == '4':
        comp = 'Lizard'
    elif comp_move == '5':
        comp = 'Spock'
    compare_moves(user_move, comp_move, comp)

#compare moves
def compare_moves(user_move, comp_move, comp):
    if user_move == '1':
        user = 'Rock'
        if comp_move == '2' or comp_move == '5':
            comp_win = True
        elif comp_move == '1':
            comp_win = 'Tie'
        else:
            comp_win = False
    elif user_move == '2':
        user = 'Paper'
        if comp_move == '3' or comp_move == '4':
            comp_win = True
        elif comp_move == '2':
            comp_win = 'Tie'
        else:
            comp_win = False
    elif user_move == '3':
        user = 'Scissors'
        if comp_move == '1' or comp_move == '5':
            comp_win = True
        elif comp_move == '3':
            comp_win = 'Tie'
        else:
            comp_win = False
    elif user_move == '4':
        user = 'Lizard'
        if comp_move == '3' or comp_move == '1':
            comp_win = True
        elif comp_move == '4':
            comp_win = 'Tie'
        else:
            comp_win = False
    elif user_move == '5':
        user = 'Spock'
        if comp_move == '2' or comp_move == '4':
            comp_win = True
        elif comp_move == '5':
            comp_win = 'Tie'
        else:
            comp_win = False
    #display move selections
    print('\nYou chose', user + '.', '\nThe computer chose', comp + '.')
    display_winner(comp_win, user, comp)

#display winner
def display_winner(comp_win, user, comp):
    if comp_win == True:
        print(comp, 'beats', user + '.')
        print('\nYou Lose.')
    elif comp_win == False:
        print(user, 'beats', comp + '.')
        print('\nYou Win.')
    else:
        print('\nIt\'s a tie.')
    gameOver()

#initial run
beginGame()
