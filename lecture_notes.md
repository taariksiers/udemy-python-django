# Section 16: Django Level One - Basics

## Check Django version
```bash
python -m django --version
```

## Add Django project

```bash
cd src
django-admin startproject [project_name]
```

## Create app
```bash
cd [project_dir]
python manage.py startapp [app_name]
```

## Start project

```bash
cd [project_dir]
python manage.py runserver
```

## Run migration

```bash
python manage.py migrate
```

# Section 17 -  Django Level Two

## Lecture 128 - Creating Models

```bash
python manage.py makemigrations [appname]
python manage.py migrate
```

### Using the shell to check if the migration ran successfully
```bash
python manage.py shell
```
Then
```python
from first_app.models import Topic
print(Topic.objects.all()) # no results
t = Topic(top_name='Social Network')
t.save()
print(Topic.objects.all())
# <QuerySet [<Topic: Social Network>]>
quit()
```
Create a [superuser](README.md#Super-User)
```bash
python manage.py createsuperuser
```

## Lecture 129 - Population Scripts
Install faker (already done via [requirements](README.md#requirementstxt))

## Lecture 130:132 - Model View Templates

```bash
# migration
./manage.py makemigrations && ./manage.py migrate
# populating
python populate_users.py
# rollback
./manage.py migrate first_app 0001_initial
```

## Lecture 135:138 - Forms

```bash
django-admin startproject basicforms
django-admin startapp basicapp
```

# Section 19 - Django Level Four

## Lecture 140-146

```bash
mkdir -p src/django_level_four && cd src/django_level_four
django-admin startproject learning_templates
django-admin startapp basic_app
mkdir -p basic_app/templates/basic_app

# Lecture 141
./src/django_level_four/learning_templates/manage.py runserver
./src/django_level_four/learning_templates/manage.py migrate
./src/django_level_four/learning_templates/manage.py createsuperuser
/Users/taarik.siers/Workspace/udemy-python-django/lecture_notes.md
```
