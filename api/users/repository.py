from django.contrib.auth import get_user_model

from users.models import User


class UserRepository:
    def __init__(self, user_model=get_user_model()):
        self._user_model = user_model


    def get_user(self, telegram_id: int) -> User:
        try:
            return self._user_model.objects.get(telegram_id=telegram_id)

        except self._user_model.DoesNotExist:
            return self.create_user(telegram_id)


    def create_user(self, telegram_id: int) -> User:
        return self._user_model.objects.create(telegram_id=telegram_id)
