import random

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(random.sample(question_bank, 4))

while quiz.still_has_questions():
    quiz.next_question()

print(f"quiz ended, your score was {quiz.score}/{len(quiz.question_list)}")