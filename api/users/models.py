from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class CustomUserManager(BaseUserManager):

    def create_user(self, telegram_id, password=None, **extra_fields):
        user = self.model(telegram_id=telegram_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, telegram_id, password=None, **extra_fields):
        user = self.create_user(telegram_id, password, **extra_fields)
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    telegram_id = models.BigIntegerField(primary_key=True, unique=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'telegram_id'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.telegram_id)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True