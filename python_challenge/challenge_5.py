#!/usr/bin/env python3

import pickle

data = pickle.load(open('banner.p', 'rb'))
for line in data:
    print(''.join([key * value for key, value in line]))
    
# ANSWER: channel
