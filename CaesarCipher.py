#!/usr/bin/env python3
# Caesar Cipher

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                                                         
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, cipher_shift):
    cipher_text = ""
    #Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    for letter in plain_text:
        if letter not in alphabet:
            cipher_text += letter
            continue
        if alphabet.index(letter) + cipher_shift > len(alphabet) - 1:
            index = (alphabet.index(letter) + cipher_shift) - len(alphabet)
        else:
            index = alphabet.index(letter) + cipher_shift
        cipher_text += alphabet[index]

    print(cipher_text)

def decrypt(cipher_text, cipher_shift):
    plain_text = ""
    for letter in cipher_text:
        if letter not in alphabet:
            plain_text += letter
            continue
        if alphabet.index(letter) - cipher_shift < 0:
            index = (alphabet.index(letter) - cipher_shift) + len(alphabet)
        else:
            index = alphabet.index(letter) - cipher_shift
        plain_text += alphabet[index]

    print(plain_text)

#print logo
print(logo)

#prompt user for inputs
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

if direction.lower() == "encode":
    text = input("Type your message:\n").lower().strip()
    shift = int(input("Type the shift number:\n"))
    #Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
    encrypt(text, shift)
elif direction.lower() == "decode":
    text = input("Type your message:\n").lower().strip()
    shift = int(input("Type the shift number:\n"))
    decrypt(text, shift)
else:
    print("Terminal error:", direction, "is not a valid operation.")

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