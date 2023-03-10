#!/usr/bin/env python3
# State Names

# Imports
from PIL import Image
import turtle
import pandas

# Constants
IMAGE = 'blank_states_img.gif'

# Named states counter
named_states = 0

# Create screen
screen = turtle.Screen()
screen.title('State Names')

# Create turtle
t = turtle.Turtle()
t.speed('fastest')
t.hideturtle()
t.penup()

# Set screen size
img = Image.open(IMAGE)
w, h = img.size
print(w, h)
screen.setup(width=w, height=h)

# Set background
screen.bgpic(IMAGE)

# Read csv data
state_data = pandas.read_csv('50_states.csv')

# Prompt controller
def prompt_for_states(x, y):
    global named_states
    while named_states < 50:
        # Prompt user for state name
        user_input = screen.textinput(title=str(named_states) + '/50', prompt='Enter a state:')

        # Handle exit
        if user_input is None:
            break

        # Check user input is valid state
        state_name = str(user_input).strip().title()
        state = state_data[state_data['state'] == state_name]
        if not state.empty:
            t.setpos(x=int(state.iloc[0]['x']), y=int(state.iloc[0]['y']))
            t.write(state.iloc[0]['state'])
            named_states += 1
            state_data.drop(state.index)        

# Listen for screen click
screen.onclick(prompt_for_states)

# Begin prompting
prompt_for_states(0, 0)

# Turtle main loop
turtle.mainloop()

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