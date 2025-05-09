from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from quiz_brain import score
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(qtext=question_text, qanswer=question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions:
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")