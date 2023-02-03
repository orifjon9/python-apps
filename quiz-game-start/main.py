from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank: list[Question] = []
for item in question_data:
    q = Question(item['text'], item['answer'])
    question_bank.append(q)

quiz = QuizBrain(question_bank)
while quiz.has_any_questions():
    nxt_question = quiz.next_question()

    user_answer = input(f'Q.{quiz.pos}: {nxt_question.text} (True/False)?: ')
    quiz.check_answers(user_answer, nxt_question.answer)

quiz.report()
