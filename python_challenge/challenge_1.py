#!/usr/bin/env python3

encrypted = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
decrypted = ''
for letter in encrypted:
    num = ord(letter) + 2
    if letter == ' ' or letter == '(' or letter == ')' or letter == '.':
        num = ord(letter)
    if chr(num) == '{':
        decrypted += 'a'
    else:
        decrypted += chr(num)
print(decrypted)

# ANSWER: ocr
