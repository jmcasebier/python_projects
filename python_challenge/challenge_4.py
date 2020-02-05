#!/usr/bin/env python3

from urllib.request import *
import re

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
num = str(16044 / 2)


while True:

    data = urlopen(url % num).read().decode()
    print(data)
    match = re.search('and the next nothing is (\d+)', data)
    num = match.group(1)

# ANSWER: peak
