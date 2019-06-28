#!/usr/bin/env python3

#imports
from random import randint

guessesTaken = 0

print('Hello! What is your name?')
name = input()

number = randint(1, 20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 5:
    if guessesTaken == 0:
        print('Take a guess.')
    else:
        print('Take another guess.')

    guess = int(input())
    guessesTaken += 1

    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + name + '! You guessed the number in ' +
    guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
