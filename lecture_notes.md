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

<hr>

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

## Lecture 138
appTwo / ProTwo


<hr>

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
```

<hr>

# Section 20 - Django Level Five - Authentication

## Lecture 147-154 - [Slides](https://docs.google.com/presentation/d/1uKZ61h4A_tfv9Nz_YYnQJfzpJVxooB5QCGtDJq2eVks/edit#slide=id.g1ed58b0fce_0_28)

### Lecture 148
```bash
mkdir -p src/django_level_five && cd src/django_level_five
django-admin startproject learning_users
cd learning_users
mkdir -p templates/basic_app static media/profile_pics
django-admin startapp basic_app

./manage.py migrate
./manage.py makemigrations basic_app
./manage.py migrate

python -m pip install bcrypt
python -m pip install django[argon2]
```

### Lecture 151
Mark `learning_users` as sources root in Pycharm. Exclude `django_level_four` `learning_templates` directory (same app name).

```bash
python -m pip install pillow
./manage.py makemigrations basic_app
./manage.py migrate
```

<hr>

# Section 22 - Advanced Topics - CBVs

## Lecture 159 - 163

```bash
django-admin startproject advcbv
django-admin startapp advanced_section

./manage.py migrate
./manage.py makemigrations basic_app
./manage.py migrate

`./manage.py createsuperuser`

```

# Section 23 - First Clone Project

## Lecture 164 - 174

```bash
django-admin startproject mysite
cd mysite
django-admin startapp blog
touch mysite/urls.py mysite/forms.py

./manage.py migrate
./manage.py makemigrations blog
./manage.py migrate

./manage.py createsuperuser
```

<hr>

# Section 24 - Social Media Site Clone

## Lecture 175 - 178

```bash
mkdir -p simple_social_clone && cd simple_social_clone
django-admin startproject simplesocial
cd simplesocial
django-admin startapp accounts
mkdir -p templates
mkdir -p static/simplesocial/css
mkdir -p static/simplesocial/js
mkdir -p static/css
mkdir -p static/images
touch static/css/main.css

./manage.py migrate
./manage.py makemigrations
./manage.py migrate
./manage.py runserver
```

## Lecture 179

```bash
./manage.py makemigrations accounts
./manage.py migrate

./manage.py createsuperuser # admin hello123
```

## Lecture 180

```bash
cd simple_social_clone/simplesocial
django-admin startapp posts
django-admin startapp groups

mkdir -p posts/templates/posts
mkdir -p groups/templates/groups

touch posts/templates/posts/post_base.html
touch posts/templates/posts/post_confirm_delete.html
touch posts/templates/posts/post_detail.html
touch posts/templates/posts/post_form.html
touch posts/templates/posts/post_list.html
touch posts/templates/posts/user_post_list.html
touch posts/templates/posts/_post.html

touch posts/forms.py
touch posts/urls.py

touch groups/templates/groups/group_base.html
touch groups/templates/groups/group_detail.html
touch groups/templates/groups/group_form.html
touch groups/templates/groups/group_list.html

touch groups/urls.py

```

## Lecture 187

```bash

./manage.py makemigrations
./manage.py migrate

```

## Lecture 188

https://stackoverflow.com/questions/70319606/importerror-cannot-import-name-url-from-django-conf-urls-after-upgrading-to


## Lecture 188

https://stackoverflow.com/questions/27213752/collecting-staticfiles-throws-improperlyconfigured

<hr>

# Section 25 - Debug Toolbar

## Lecture 189

`settings.py`

```python
INSTALLED_APPS = [
     'django.contrib.sessions',
     'django.contrib.messages',
     'django.contrib.staticfiles',
+    'debug_toolbar',
     'appTwo'
 ]

MIDDLEWARE = [
     'django.contrib.auth.middleware.AuthenticationMiddleware',
     'django.contrib.messages.middleware.MessageMiddleware',
     'django.middleware.clickjacking.XFrameOptionsMiddleware',
+    'debug_toolbar.middleware.DebugToolbarMiddleware',
 ]

 INTERNAL_IPS = ['127.0.0.1']
 ```

<hr>

# Section 26 - Advanced Topics: Customising the Django Admin

Lectures 191 - Lecture 197

## Lecture 191


```bash

django-admin startproject my_video_rental

cd my_video_rental/

django-admin startapp videos

```

Edit `settings.py`

- add to `INSTALLED_APPS`
- update general settings inline with previous lectures

Add models (`Movie` and `Customer`)

Add models to admin register (`admin.py`)

Make and run migrations, add super user and run server

```bash
./manage.py makemigrations && ./manage.py migrate videos
./manage.py createsuperuser
./manage.py runserver
```

Add some more custom stuff to the models

## Lecture 192

```bash
cd src/my_video_rental
mkdir -p templates/admin
```

Go to https://github.com/django/django/tree/main/django/contrib/admin/templates