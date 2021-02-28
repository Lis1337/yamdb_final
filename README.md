# YaMDB_final

Учебынй проект в рамках Яндекс.Практикума.
На YaMDb читатели оставляют к произведениям текстовые отзывы и выставляют рейтинг.

## Готовясь к запуску

Эти инструкции позволят вам запустить копию проекта на вашем локальном компьютере в целях разработки и тестирования.
Образ postgres [DockerHub](https://hub.docker.com/_/postgres).
Образ nginx [DockerHub](https://hub.docker.com/_/nginx).

## Требования

Перед запуском работы проверьте наличие 
[Python](https://www.python.org/downloads/),
[Django](https://www.djangoproject.com/), 
[Docker](https://www.docker.com/).

## Установка

*Клонируйте репозиторий на локальный компьютер. 
Выполните сборку контейнера.*
```
$ docker-compose build
```

*Запуск docker-compose.*
```
$ docker-compose up
```
При создании контейнера миграции выполнятся автоматически.

## Использование контейнера.

*Создание суперпользователя и инициализация данных.*

```sh
$ docker-compose exec web  python manage.py collectstatic
$ docker exec -it <CONTAINER ID> python manage.py makemigrations
$ docker exec -it <CONTAINER ID> python manage.py migrate
$ docker exec -it <CONTAINER ID> python manage.py createsuperuser
$ docker exec -it <CONTAINER ID> python manage.py loaddata fixtures.json
```
## Выключение контейнера.
```
docker-compose down
```
## Удаление контейнеров.
```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```
![yamdb_final workflow](https://github.com/lis1337/yamdb_final/workflows/yamdb_final%20workflow/badge.svg)
