edit .env

docker exec api python manage.py migrate

Добавление вопросов по пути /home/questions_bot/questions.txt:
docker exec api python manage.py add_questions /app/api/questions.txt
