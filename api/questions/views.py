from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from questions.repository import QuestionRepository
from questions.services import QuestionService
from users.repository import UserRepository


class GetRandomQuestion(APIView):
    service = QuestionService
    user_repo = UserRepository
    question_repo = QuestionRepository

    def get(self, request, telegram_id):
        service = self._create_question_service()

        try:
            question = service.get_question(telegram_id)

            if question:
                return Response(
                    data={'data': question.question},
                    status=status.HTTP_200_OK
                )

            return Response(
                data={'data': 'У матросов нет вопросов'},
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:
            return Response(
                data={'data': e},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def _create_question_service(self):
        return self.service(
            user_repo=self.user_repo,
            question_repo=self.question_repo
        )
