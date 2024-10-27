import random
from typing import Optional

from questions.models import Question, QuestionAnswers


class QuestionService:
    def __init__(self, user_repo, question_repo):
        self.user_repo = user_repo()
        self.question_repo = question_repo()

    def get_question(self, telegram_id: int) -> Optional[Question]:
        user = self.user_repo.get_user(telegram_id)
        question = self._get_random_question(user)
        QuestionAnswers.objects.create(question=question, user=user)
        return question

    def _get_random_question(self, user) -> Optional[Question]:
        questions = self.question_repo.get_not_answered(user)
        if questions:
            return random.choice(questions)