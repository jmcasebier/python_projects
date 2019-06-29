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

#get player name
def meet_player():
    clear()
    print('Hello! What is your name?')
    return input()

#introduce game
def greet_player():
    print('Well, ' + player + ', I am thinking of a number between 1 and 20.')

#start new game with same player
def play_again():
    clear()
    print('Ok, ' + player + ', let\'s play again!')
    print('I\'m thinking of a number between 1 and 20')
    begin_game()

#choose number and begin game
def begin_game():
    guessesTaken = 0
    guesses = []
    number = randint(1, 20)
    while guessesTaken < 5:
        #get guess from user
        if guessesTaken == 0:
            print('Take a guess.')
        else:
            print('Take another guess.')

        guess = int(input())

        #allow each number to be guessed only once
        while guess in guesses:
            print('You already guessed ' + str(guess) +'.')
            print('Try a different number.')
            guess = int(input())

        #update game variables
        guessesTaken += 1
        guesses.append(guess)

        #give user feedback about guess
        if guess < number and guessesTaken <= 4:
            print('Your guess is too low.')
        if guess > number and guessesTaken <= 4:
            print('Your guess is too high.')
        if guess == number:
            break

    #user guessed number
    if guess == number:
        if guessesTaken == 1:
            message = ' guess!'
        else:
            message = ' guesses!'
        guessesTaken = str(guessesTaken)
        print('Good job, ' + player + '! You guessed the number in ' +
        guessesTaken + message)
        game_over()

    #user ran out of guesses
    if guess != number:
        number = str(number)
        print('Nope. The number I was thinking of was ' + number + '.')
        game_over()

#play again or exit
def game_over():
    print('Would you like to play again? (y / n)')
    again = input()
    y_n = ['y', 'n']
    while again.lower() not in y_n:
        print('I don\'t understand.')
        print('Please enter \'y\' to play again or \'n\' to exit.')
        again = input()
    if again.lower() == 'y':
        play_again()
    else:
        clear()
        exit()

#initialize and play
player = meet_player()
greet_player()
begin_game()
