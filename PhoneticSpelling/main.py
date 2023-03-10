#!/usr/bin/env python3
# Phonetic Spelling

# LIST COMPREHENSION
# new_library = [item for item in list if condition]

# DICTIONARY COMPREHENSION
# new_dictionary = {new_key: new_value for item in list if condition}
# new_dictionary = {new_key: new_value for (key, value) in dictionary.items() if condition}

# Imports
import pandas

# Read csv data
phonetic_alphabet_df = pandas.read_csv('nato_phonetic_alphabet.csv')

# Create dictionary
phonetic_alphabet = {row.letter: row.code for (index, row) in phonetic_alphabet_df.iterrows()}

# Prompt user for a word
user_input = input('Enter a word: ').strip().upper().split(' ')[0]

# Display phonetic spelling
try:
    phonetic_spelling = [phonetic_alphabet[letter] for letter in user_input]
    print(phonetic_spelling)
except KeyError as ke:
    print('Invalid character:', ke)

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