## Проект YaMDb

Выполнен в рамках курса Python-разработчик от Яндекс.Практикум.

Модуль: Управление проектом на удаленном сервере.

## Инструменты:

<p align="left"> <img src="https://img.icons8.com/fluency/48/000000/python.png" alt="python" width="40" height="40"/> </a> <a href="" target="_blank"> <img src="https://img.icons8.com/color/48/000000/django.png" alt="django" width="40" height="40"/> </a> <a href=" target="_blank"> <img src="https://img.icons8.com/dusk/64/000000/docker.png" alt="docker" width="40" height="40"/> </a><a href=" target="_blank"> <img src="https://img.icons8.com/color/48/000000/nginx.png" alt="nginx" width="40" height="40"/> </a>
  

## Описание:

В проекте YaMDb реализован API с помощью Django REST Framework, его задача
собирать отзывы (Review) пользователей на произведения (Titles). Пользователи
оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку
в диапозоне от одного до десяти (целое число). На одно произведение пользователь
может оставить только один отзыв.


## Как запустить проект:
Перейти в папку /infra
Запустить: 
```shell
docker-compose up -d --build
```

Применить миграции:
```shell
docker-compose exec web python manage.py migrate
```

Создать суперпользователя:
```shell
docker-compose exec web python manage.py createsuperuser
```
Cобрать статические файлы:
```shell
docker-compose exec web python collecstatic --no-input
```

## Основные доступные эндпоинты можно посмотреть по адресу:
```shell
✨ http://localhost/redoc
```

