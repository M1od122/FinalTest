# API для управления перевалами

Этот проект представляет собой REST API для управления перевалами. API позволяет добавлять, получать и редактировать данные о перевалах.

## Оглавление
- [Описание](#описание)
- [Технологии](#технологии)
- [Установка](#установка)
- [Переменные окружения](#переменные-окружения)
- [Использование API](#использование-api)
  - [Добавление перевала](#добавление-перевала)
  - [Получение перевала по ID](#получение-перевала-по-id)
  - [Редактирование перевала по ID](#редактирование-перевала-по-id)
- [Тестирование](#тестирование)

## Описание

Этот REST API предоставляет конечные точки для управления данными о перевалах. Вы можете добавлять новые перевалы, получать информацию по существующим перевалам и редактировать данные.

## Технологии

- Python
- Django
- Django REST Framework
- PostgreSQL (или другая реляционная СУБД, поддерживаемая библиотекой psycopg2)

## Установка

Следуйте этим шагам для установки и запуска проекта:

1. Клонируйте репозиторий:
bash
   git clone https://github.com/ваше_имя/ваш_репозиторий.git
   cd ваш_репозиторий
   
2. Создайте и активируйте виртуальное окружение:
bash
   python -m venv venv
   source venv/bin/activate  # для Unix или macOS
   venv\Scripts\activate  # для Windows
   
3. Установите зависимости:
bash
   pip install -r requirements.txt
   
4. Создайте файл `.env` в корне проекта и добавьте следующие переменные окружения:
plaintext
   FSTR_DB_HOST=your_db_host
   FSTR_DB_PORT=your_db_port
   FSTR_DB_LOGIN=your_db_login
   FSTR_DB_PASS=your_db_password
   
5. Проведите миграцию базы данных:
bash
   python manage.py migrate
   
6. Запустите сервер:
bash
   python manage.py runserver
   
## Переменные окружения

Для работы приложения необходимы следующие переменные окружения, которые должны быть указаны в файле `.env`:
- `FSTR_DB_HOST`: Хост базы данных.
- `FSTR_DB_PORT`: Порт базы данных.
- `FSTR_DB_LOGIN`: Логин для доступа к базе данных.
- `FSTR_DB_PASS`: Пароль для доступа к базе данных.

## Использование API

### Добавление перевала

- **Метод**: `POST`
- **URL**: `/submitData/`

#### Пример тела запроса:
json
{
    "name": "Test Pass",
    "coordinates": "45.0, 30.0",
    "height": 1000,
    "user_name": "John Doe",
    "user_email": "john.doe@example.com",
    "user_phone": "1234567890",
    "photos": ["http://example.com/photo1.jpg"]
}
#### Ответ:
json
{
    "status": 200,
    "message": "Отправлено успешно",
    "id": 1  // Возвращаемый ID нового перевала
}
### Получение перевала по ID

- **Метод**: `GET`
- **URL**: `/submitData/<id>/`

### Редактирование перевала по ID

- **Метод**: `PATCH`
- **URL**: `/submitData/edit/<id>/`

#### Пример тела запроса:
json
{
    "name": "Updated Test Pass"
}
## Тестирование

Для запуска тестов в проекте выполните следующее:
bash
python manage.py test



