#!/usr/bin/env python3
# Trivia

# Imports
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# List of trivia questions
question_bank = []

# Append questions as Question objects
for trivia_question in question_data:
    question_bank.append(Question(trivia_question['text'], trivia_question['answer']))

# Quiz controller object
quiz = QuizBrain(question_bank)

# Run quiz
while quiz.still_has_questions():
    user_answer = quiz.next_question()
    quiz.check_answer(user_answer)
    print()
    print()

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