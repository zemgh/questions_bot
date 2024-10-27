from django.contrib import admin

from questions.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']
    search_fields = ['question']
    labels = {
        'question': 'Вопрос',
        'answer': 'Ответ'}

    fields = ['question', 'answer']
