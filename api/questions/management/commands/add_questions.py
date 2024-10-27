import os

from django.core.management.base import BaseCommand
from django.db import transaction, IntegrityError

from questions.models import Question


class Command(BaseCommand):
    help = 'Add questions from .txt'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='Путь к текстовому файлу')

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']

        if not os.path.isfile(filename):
            self.stdout.write(self.style.ERROR(f'Файл {filename} не существует.'))
            return

        with open(filename, 'r') as f:
            for line in f:
                question = line.strip()

                if question:
                    self._write_to_db(question)

    @transaction.atomic
    def _write_to_db(self, question):
        try:
            Question.objects.create(question=question)
            self.stdout.write(self.style.SUCCESS(f'Добавлен вопрос: {question}'))

        except IntegrityError:
            self.stdout.write(self.style.WARNING(f'Вопрос уже существует:. {question}'))

        except Exception as e:
            self.stdout.write(self.style.WARNING(str(e)))
