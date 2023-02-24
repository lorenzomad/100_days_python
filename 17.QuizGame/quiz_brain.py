class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        """ask the next question and updates the score"""
        current_question = self.question_list[self.question_number]
        user_answer = input(
            f"Q.{str(self.question_number + 1)}: {current_question.text} (True/False):"
            )
        self.check_answer(user_answer, current_question.answer)
        self.question_number += 1


    def still_has_questions(self):
        """returns true if there are questions left, else false"""
        return self.question_number < len(self.question_list) 

    def check_answer(self, user_answer, correct_answer):
        """increases the score if the answer is correct"""
        if correct_answer.lower() == user_answer.lower():
            print("correct!")
            self.score += 1
        print(f"the correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number+1}\n")
    