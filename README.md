# yamdb_final
API для сбора отзывов пользователей на различные произведения (проект Яндекс.Практикум)

![workflow](https://github.com/legyan/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Оглавление
1. [Описание](#Описание)
2. [Стек технологий](#Стек_технологий)
3. [Команда разработки](#Команда_разработки)
4. [Как запустить проект](#Как_запустить)
5. [Эндпоинты API](#Эндпоинты)
6. [Примеры запросов](#Примеры_запросов)
      1. [Публикация нового произведения](#Публикация_произведения)
      2. [Запрос списка категорий](#Список_категорий)
      3. [Запрос списка жанров](#Список_жанров)
      4. [Изменение данных своей учетной записи](#Данные_учетной_записи)

<a name="Описание"></a> 
## Описание

Проект YaMDb собирает отзывы пользователей на произведения. Произведения относятся к одной из трёх категорий: книги, фильмы или музыка. В каждой категории есть произведения: книги, фильмы или музыка. Произведению может быть присвоен жанр из списка предустановленных или созданных администратором. Пользователи могут оставлять к произведениям текстовые отзывы и ставить произведению оценку в диапазоне от одного до десяти. Из пользовательских оценок формируется усреднённая оценка произведения — рейтинг. Также есть возможность комментирования отзывов.

<a name="Стек_технологий"></a> 
## Стек технологий 


![python version](https://img.shields.io/badge/Python-3.8-yellowgreen) 

![python version](https://img.shields.io/badge/Django-2.2.16-yellowgreen)

![python version](https://img.shields.io/badge/djangorestframework-3.12.4-yellowgreen) 

<a name="Команда_разработки"></a> 
## Команда разработки

1. [Дмитрий Кургузиков](https://github.com/the-man-with-no-memory)
Система регистрации и аутентификации, права доступа, работа с токеном, система подтверждения через e-mail.

2. [Кирилл Шалыгин](https://github.com/just4fun-xd)
Категории, моделии жанры (модели, представления и эндпоинты к ним).

3. [Левон Гегамян](https://github.com/Legyan)
Отзывы и комментарии (модели, представления и эндпоинты к ним), рейтинги произведений и механизм импорта данных из csv файлов в бау данных.

[Документация API с примерами запросов (yaml)](https://github.com/the-man-with-no-memory/api_yamdb/blob/master/api_yamdb/static/redoc.yaml)

На запущенном проекте документация доступна по адресу: [```/redoc/```](http://127.0.0.1:8000/redoc/)

<a name="Как_запустить"></a> 
## Как запустить проект:

Клонировать репозиторий:

```
git clone https://github.com/Legyan/infra_sp2
```

Перейти в директорию для разворачиания проекта:

```
cd infra/
```

Перед разворачиванием проекта необходимо добавить в директорию .env файл, заполненый по следующему шаблону:

```
DB_ENGINE=#### 
DB_NAME=####
POSTGRES_USER=####
POSTGRES_PASSWORD=####
DB_HOST=####
DB_PORT=####
SECRET_KEY=####
```

Собрать и запустить docker-compose:

```
docker-compose up -d --build
```

Выполнить миграции:

```
sudo docker-compose exec web python manage.py migrate
```

Загрузить данные в базу из csv файлов:

```
sudo docker-compose exec web python manage.py load_from_csv
```

Подгрузить статические файлы:

```
sudo docker-compose exec web python manage.py collectstatic --no-input
```

Проверить доступность приложения по адресу http://localhost

<a name="Эндпоинты"></a> 
## Некоторые Эндпоинты API

api/v1/titles/ (GET, POST, PUT, PATCH, DELETE): произведения пользователей;

api/v1/categories/ (GET): категории произведений;

api/v1/genres/ (GET): жанры;

api/v1/users/me/ (GET, PATCH): Получение/изменения данных своей учетной записи

<a name="Примеры_запросов"></a> 
## Примеры запросов

<a name="Публикация_произведения"></a> 
### Публикация нового произведения

Эндпоинт:

`api/v1/titles/ `

Запрос POST:

```
{

    "name": "Сияние",
    "year": 1977,
    "description": "В каждом крупном отеле бывают скандалы, и привидения в каждом крупном отеле имеются.",
    "genre": [
        "horrors"
        ],
    "category": "books"
}

```

Ответ:

```
{
    "id": 1,
    "name": "Сияние",
    "year": 1977,
    "description": "В каждом крупном отеле бывают скандалы, и привидения в каждом крупном отеле имеются.",
    "genre": [
        "horrors"
    ],
    "category": "books"
}
```

<a name="Список_категорий"></a> 
### Запрос списка категорий

Эндпоинт:

`api/v1/categories/ `

Запрос GET

Ответ:

```
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "Книги",
            "slug": "books"
        },
        {
            "name": "Песни",
            "slug": "songs"
        },
        {
            "name": "Фильмы",
            "slug": "films"
        }
    ]
}
```

<a name="Список_жанров"></a> 
### Запрос списка жанров

Эндпоинт:

`api/v1/genres/ `

Запрос GET

Ответ:

```
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "Комедии",
            "slug": "comedy"
        },
        {
            "name": "Романы",
            "slug": "novels"
        },
        {
            "name": "Ужасы",
            "slug": "horrors"
        }
    ]
}
```

<a name="Данные_учетной_записи"></a> 
### Изменение данных своей учетной записи

Эндпоинт:

`api/v1/users/me/`

Запрос PATCH

```
{
    "first_name": "Walter",
    "last_name": "White",
    "bio": "chemist"
}
```

Ответ:

```
{
    "username": "admin",
    "email": "admin@admin.com",
    "first_name": "Walter",
    "last_name": "White",
    "bio": "chemist",
    "role": "admin"
}
```
