# Сайт ФИСТ УлГТУ

## Задачи
### Общее описание
Далее в разделе Backlog выложены основные подразделы сайта, которые необходимо реализовать.

В каждом разделе описаны сущности. Это не таблицы БД, хотя и могут описывать структуру таблиц. В любом случае нормализацию необходимо провести.

Выполнение задания подразумевает 3 этапа: проектирование, реализация, наполнение данными (часть реальных данных) и тестирование.

Выполнять задания можно группами из двух человек.

На этапе проектирования и разработки:
1. Описать обобщенную постановку задачи в 3 относительно коротких предложения:
1.1. Что вы делаете и зачем это нужно. Тут необходимо описать объект проектирования с точки зрения его ценности для конечного пользователя.
1.2. Как вы это делаете? Здесь нужно подумать над методом, используемым в процессе разработки. Например, метод comet - опишите основные этапы проекирования.
1.3. Какими инструментами вы это делаете. Тут можно описать
2. Описать диаграмму вариантов использования, ER-иаграмму, диаграму классов и прототип пользовательского интерфейса (figma или непосредственно верстка)
3. Утвердить педлагаемые решения у преподавателя.
4. Реализовать предложенный модуль в программном коде. За основу необходимо взять проект https://github.com/ksvyatov/csdprt и встроить свои решения в существующую структуру уже подготовленного сайта, включая меню. 
5. Создать pull request для применения изменений в основную ветку проекта.
6. Показать проект на защите проектов.

### Backlog
#### 1. Блог
Воозможность писать статьи, которые могут быть оформлены как отдельные страницы, либо как новости
* Теги (id, name, description, author, date) - для создания рубрикатора и облака тегов, которые связывают многие сущности между собой (статьи, проекты, дисциплины, преподаватели)
* Статьи (id, title, text (wysiwyg), tags[], author, date, comments)
* Типы статей (id, name, title)

#### 2. FIST ideas
Идеи проектов, которые могут быть реализованы студентами, у которых не хватает идей для реализации, или кому-то хочется что-то реализовать, но не хватает рук.
Здесь необходимо проводить модерацию перед опубликованием.
* Ideas (id, title, description, tags[], likes, dislikes, comments, goal, methods, technologies, is_moderated, moderator, projects)


#### 4. Projects
Проекты, которые реализуются на факультете
* Labs (id, description, address, tags[], areas[], )
* Projects (id, description, tags[], posts[], areas[], lab, comments)
* Areas (id, title, description) - области исследований (например, ML, robotics, ...)

#### 6. Events
Мероприятия, которые проводятся на факультете. Важно сделать календарь событий во фронтовой части (представления за месяц/неделю/день)
* Events (id, title, event_type, description, date_start, date_end, tags[], participants[], projects[], areas[], parent_event)
* EventTypes (id, title, name)

#### 7. Трудоустрйоство и партнерства
* Vacancies - список вакансий (структуру описания вакансии можно взять с hh.ru)
* CVs - резюме тех людей, которые хотят найт работу.
Необходимо задействовать ссылки на лаборатории, теги, проекты, идеи, статьи блога
* Persons - преподаватели (почти готово уже)
* Partners (id, name, address, persons, programs, tags, projects) - компании-партнеры

#### 8. Структура факультета
* Departments (id, name, descritption, history, persons, labs, events, projects) - кафедры
* Programs (id, name, description, program_type, duration, partners) - направления подготовки
* Program types (id, name, description) - типы направлений подготовки
* Disciplines  (id, name, description, tags, mooc_url, tags, projects, persons, course_num, has_exam, has_mark, has_course_work, lectures_hrs_num, practice_hrs_num, total_hrs_num) - дисциплины



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

