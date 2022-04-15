# hello
## hello
**hello**
*hello*
~hello~
>hello

Some basic Git commands are:
```
git status
git add
git commit
```
`hello`
# api_final_yatube

**Приложение предоставляет собственное api со следующим функционалом:**

-авторизация пользователя

-добавление, изменение и удаление постов и комментариев к ним

-возможность подписаться на других пользователей

-присутствуют несколько уровней разрешения

-возможность фильтрации и поиска


### Автор: Василий - студент Яндекс Практикума.

### Примеры эндпойнтов, доступых их приложения

`GET   api/v1/posts/`   *в ответе вернет список постов*

`GET   api/v1/posts/1/comments/1/`    в ответе вернет объект первого 
комментария первого поста

`POST  api/v1/posts/`  создаст новый пост, если данные в запросе валидны

`POST  api/v1/groups/`  вернет ошибку 405, т.к. создание группы через api не доступно.

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

`git clone https://github.com/yandex-praktikum/kittygram.git`

`cd kittygram`

Cоздать и активировать виртуальное окружение:

`python3 -m venv env`

`source env/bin/activate`

Установить зависимости из файла requirements.txt:

`python3 -m pip install --upgrade pip`

`pip install -r requirements.txt`

Выполнить миграции:

`python3 manage.py migrate`

Запустить проект:

`python3 manage.py runserver`
