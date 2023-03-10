#!/usr/bin/env python3
# Coffee Machine

# Imports
from datetime import datetime
from moneyed import Money, USD
from os import system

# Machine power
power_on = True

# Coffer monies
coffer = Money('0.00', USD)

# Drink menu
MENU = {
    'espresso': {
        'ingredients': {
            'water': 50, # mL
            'coffee': 18, # g
        },
        'cost': Money('1.50', USD)
    },
    'latte': {
        'ingredients': {
            'water': 200, # mL
            'milk': 150, # mL
            'coffee': 24, # g
        },
        'cost': Money('2.50', USD)
    },
    'cappuccino': {
        'ingredients': {
            'water': 250, # mL
            'milk': 100, # mL
            'coffee': 24, # g
        },
        'cost': Money('3.00', USD)
    }
}

# Machine resources
resources = {
    'water': 300, # mL
    'milk': 200, # mL
    'coffee': 100, # g
}

# Clear console
system("cls")

def make_espresso():
    # Make espresso
    espresso = MENU['espresso']
    global resources
    if not resources['water'] >= espresso['ingredients']['water'] or not resources['coffee'] >= espresso['ingredients']['coffee']:
        print('Espresso drink is currently unavailable: insufficient resources.\n')
    else:
        # Collect monies
        print('Price: $%s' % espresso['cost'].amount)
        payment = input('Payment amount: $').strip()
        try:
            payment = Money(payment, USD)
            if payment.amount >= espresso['cost'].amount:
                global coffer
                coffer += espresso['cost']
                change = payment - espresso['cost']
                print('Your change is $%s.' % str(change.amount))
                # Prepare drink
                resources['water'] -= espresso['ingredients']['water']
                resources['coffee'] -= espresso['ingredients']['coffee']
                print('Enjoy your espresso! ☕\n')
            else:
                print('Insufficient funds. Your $%s has been refunded.\n' % str(payment.amount))
        except:
            print('Invalid payment amount: $%s\n' % payment)

def make_latte():
    # Make latte
    latte = MENU['latte']
    global resources
    if not resources['water'] >= latte['ingredients']['water'] or not resources['milk'] >= latte['ingredients']['milk'] or not resources['coffee'] >= latte['ingredients']['coffee']:
        print('Latte drink is currently unavailable: insufficient resources.\n')
    else:
        # Collect monies
        print('Price: $%s' % str(latte['cost'].amount))
        payment = input('Payment amount: $').strip()
        try:
            payment = Money(payment, USD)
            if payment.amount >= latte['cost'].amount:
                global coffer
                coffer += latte['cost']
                change = payment - latte['cost']
                print('Your change is $%s.' % str(change.amount))
                # Prepare drink
                resources['water'] -= latte['ingredients']['water']
                resources['milk'] -= latte['ingredients']['milk']
                resources['coffee'] -= latte['ingredients']['coffee']
                print('Enjoy your latte! ☕\n')
            else:
                print('Insufficient funds. Your $%s has been refunded.\n' % str(payment.amount))
        except:
            print('Invalid payment amount: $%s\n' % payment)

def make_cappuccino():
    # Make cappuccino
    cappuccino = MENU['cappuccino']
    global resources
    if not resources['water'] >= cappuccino['ingredients']['water'] or not resources['milk'] >= cappuccino['ingredients']['milk'] or not resources['coffee'] >= cappuccino['ingredients']['coffee']:
        print('Cappuccino drink is currently unavailable: insufficient resources.\n')
    else:
        # Collect monies
        print('Price: $%s' % str(cappuccino['cost'].amount))
        payment = input('Payment amount: $').strip()
        try:
            payment = Money(payment, USD)
            if payment.amount >= cappuccino['cost'].amount:
                global coffer
                coffer += cappuccino['cost']
                change = payment - cappuccino['cost']
                print('Your change is $%s.' % str(change.amount))
                # Prepare drink
                resources['water'] -= cappuccino['ingredients']['water']
                resources['milk'] -= cappuccino['ingredients']['milk']
                resources['coffee'] -= cappuccino['ingredients']['coffee']
                print('Enjoy your cappuccino! ☕\n')
            else:
                print('Insufficient funds. Your $%s has been refunded.\n' % str(payment.amount))
        except:
            print('Invalid payment amount: $%s\n' % payment)

def print_report():
    # Print report
    print('****************************************')
    print('REPORT')
    print('Time: %s\n' % str(datetime.now()))
    print('MONIES')
    print('Coffer: $%s\n' % str(coffer.amount))
    print('RESOURCES')
    print('Water: %smL' % str(resources['water']))
    print('Milk: %smL' % str(resources['milk']))
    print('Coffee: %sg' % str(resources['coffee']))
    print('****************************************\n')

def turn_off():
    # Turn machine off
    print('Powering down...\n')
    global power_on
    power_on = False

def invalid_selection(user_input):
    # Handle invalid selection
    print('%s is not a valid selection.\n' % user_input)

def main():
    # Prompt user for input
    user_input = input('What would you like to order?  (espresso/latte/cappuccino):\n').strip().lower()

    # Handle user input
    if user_input == 'espresso':
        make_espresso()
    elif user_input == 'latte':
        make_latte()
    elif user_input == 'cappuccino':
        make_cappuccino()
    elif user_input == 'report':
        print_report()
    elif user_input == 'off':
        turn_off()
    else:
        invalid_selection(user_input.capitalize())

# Run coffee machine
while power_on:
    main()

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