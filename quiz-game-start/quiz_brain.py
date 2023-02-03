from question_model import Question


class QuizBrain:
    def __init__(self, questions: list[Question]) -> None:
        self.pos = 0
        self.list = questions
        self.score = 0

    def next_question(self):
        if not self.has_any_questions():
            return None

        question = self.list[self.pos]
        self.pos += 1
        return question

    def has_any_questions(self):
        return self.pos + 1 != len(self.list)

    def check_answers(self, actual: str, expected: str):
        if actual == expected:
            self.score += 1
            return True
        return False

    def report(self):
        score_percentage = round((self.score / len(self.list)) * 100, 2)
        quiz_report_text = "Congratulations. You passed!" if score_percentage >= 80 else "Sorry, you failed but you can try again"
        print(f"Your final score was {score_percentage}%. {quiz_report_text}")
