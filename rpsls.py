#!/usr/bin/env python3

#imports
from random import randint
from os import system, name

#clear screen
def clear():
    if name == 'posix':
        _ = system('clear')
    else:
        _ = system('cls')

#begin the game
def begin_game():
    clear()
    #introduce game
    print('\nWelcome to Rock-Paper-Scissors-Lizard-Spock!')
    show_moves()
    get_moves()

#present option to play again
def game_over():
    play_again = input('\nPlay again? (y or n): ')
    #verify yes or no response
    y_or_n = ('y', 'n')
    while play_again.lower() not in y_or_n:
        play_again = input('\nPlease enter y to play again or n to exit: ')

    #respond to user selection
    if play_again.lower() == 'y' or play_again.lower() == 'yes':
        begin_game()
    else:
        clear()
        exit()

#display rules on request
def show_rules():
    clear()
    rules = '\n\n  Scissors cut Paper,\n  Paper covers Rock,\n  Rock'
    rules += ' crushes Lizard,\n  Lizard poisons Spock,\n  Spock smashes '
    rules += 'Scissors,\n  Scissors decapitate Lizard,\n  Lizard eats Paper,'
    rules += '\n  Paper disproves Spock,\n  Spock vaporizes Rock,\n  and '
    rules += 'Rock crushes Scissors.\n\n'
    print('\n  *****Rules*****')
    print(rules)
    #prompt user to close rules with q
    quit_rules = input('  Press Enter to return to the game...')
    begin_game()

#introduce all possible moves
def show_moves():
    print('\n****************************')
    print('\n  1 - Rock\n  2 - Paper\n  3 - Scissors\n  4 - Lizard\n  5 - Spock'
    + '\n  # - Rules\n')
    print('****************************\n')

#prompt user for move selection
def get_moves():
    user_move = input('Make your selection: ')
    #verify user selection validity
    moves = ('1', '2', '3', '4', '5', '#')
    while user_move not in moves:
        user_move = input('\nPlease enter the number of your selection: ')

    #handle user option to show rules
    if user_move == '#':
        show_rules()
    else:
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
    game_over()

#initial run
begin_game()
