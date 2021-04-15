# Сайт ФИСТ УлГТУ

## Задачи
### Backlog
1. Блог
* Теги (id, name, description, author, date)
* Статьи (id, title, text (wysiwyg), tags[], author, date, comments)
* Типы статей (id, name, title)

2. FIST ideas
* Ideas (id, title, description, tags[], likes, dislikes, comments)

4. Projects
* Labs (id, description, address, tags[], areas[], )
* Projects (id, description, tags[], posts[], areas[], lab, comments)

5. Areas
* Areas (id, title, description)

6. Events
* Events (id, title, event_type, description, date_start, date_end, tags[], participants[], projects[], areas[], parent_event)
* EventTypes (id, title, name)

### Closed

## Ссылки 
### Настройка python + google sheets (gspread)
https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
https://buildmedia.readthedocs.org/media/pdf/gspread/latest/gspread.pdf

# Работа с docker
## Запуск docker
[Описание создания окружения](https://webdevblog.ru/kak-ispolzovat-django-postgresql-i-docker/)
```bash
docker-compose up -d --build
```

## Остановка контейнера
```bash
docker-compose down -v
```

## Миграция БД
```bash
docker-compose exec webcs python manage.py makemigrations
docker-compose exec webcs python manage.py migrate --noinput
docker-compose exec webcs python manage.py createsuperuser
```
## Просмотр логов
```bash
docker-compose logs -f
```

## Зайти в терминал docker контейнера
```bash
docker container ps -a
docker exec -it [ID] /bin/sh
```

