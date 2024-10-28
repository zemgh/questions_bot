edit .env

docker exec api python manage.py migrate

bash get_cert.sh

Добавление вопросов по пути /home/src/questions.txt:
docker exec api python manage.py add_questions /app/api/questions.txt
