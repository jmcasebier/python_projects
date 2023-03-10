class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.answered_correctly = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        return input('Q.%s: %s (True/False)?: ' % (str(self.question_number + 1), question.text)).strip().lower()

    def still_has_questions(self):
        return len(self.question_list) > self.question_number
    
    def check_answer(self, user_answer):
        if self.question_list[self.question_number].answer.lower() == user_answer:
            self.answered_correctly += 1
            print("That's right!\nYou've answered %s/%s correctly." % (str(self.answered_correctly), str(self.question_number + 1)))
        else:
            print("Sorry, that's not right. The answer was %s.\nYou've answered %s/%s correctly." % (str(self.question_list[self.question_number].answer), str(self.answered_correctly), str(self.question_number + 1)))
        self.question_number += 1
