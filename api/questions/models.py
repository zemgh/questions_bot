from django.contrib.auth import get_user_model
from django.db import models


class Question(models.Model):
    question = models.TextField(unique=True)
    answer = models.TextField(null=True, blank=True)


class QuestionAnswers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='answers')