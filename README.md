## Проект YaMDb

Выполнен в рамках курса Python-разработчик от Яндекс.Практикум.

Модуль: Управление проектом на удаленном сервере.
  

## Описание:

В проекте YaMDb реализован API с помощью Django REST Framework, его задача
собирать отзывы (Review) пользователей на произведения (Titles). Пользователи
оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку
в диапозоне от одного до десяти (целое число). На одно произведение пользователь
может оставить только один отзыв.


## Как запустить проект:

Перейти в папку /infra

Запустить: docker-compose up -d --build

Применить миграции: docker-compose exec web python manage.py migrate

Создать суперпользователя: docker-compose exec web python manage.py createsuperuser

Cобрать статические файлы: docker-compose exec web python collecstatic --no-input

## Основные доступные эндпоинты можно посмотреть по адресу http://localhost/redoc

