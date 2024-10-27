from django.db.models import QuerySet

from questions.models import Question


class QuestionRepository:
    def get_not_answered(self, user) -> QuerySet:
        answered_id_lst = self._get_answered_questions(user)
        not_answered_questions = Question.objects.exclude(id__in=answered_id_lst)
        return not_answered_questions

    def _get_answered_questions(self, user) -> list[int]:
        queryset = user.answers.all()
        answered_questions = [a.question.id for a in queryset]
        all_questions_count = Question.objects.count()

        if len(answered_questions) >= all_questions_count:
            self._clear_answers(user)
            return []

        return list(answered_questions)

    def _clear_answers(self, user):
        user.answers.all().delete()

