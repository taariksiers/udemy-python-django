# My Course notes for Udemy - Python and Django Full Stack Web Developer Bootcamp

Link: [Python and Django Full Stack Web Developer Bootcamp](https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp)

&raquo; [Lecture Notes](lecture_notes.md)

<hr>

## Assumptions

- Python version ~= 3.6


## requirements.txt

```bash
python -m pip install -r requirements-to-freeze.txt --upgrade
python -m pip freeze > requirements.txt
```
## Super User
```python
./manage.py createsuperuser [username]
```


## Stock Settings additions

Line 13 - imports

```python
import os
```

Line 18-20 - DIR setups

```python
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')
```

Line 43 - last line of `INSTALLED_APPS` - add app name

Line 56 - `LOGGING`

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    "formatters": {
        "console": {"format": "{asctime} [ {name} :: {module} ] [{levelname}] | {message}", "style": "{"}
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler', 'formatter': 'console',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'basic_app.views': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}
```

Line 85 - `TEMPLATES` - `DIR`

```python
        'DIRS': [TEMPLATE_DIR],
```

Line 136 - `TIME_ZONE`

```python
TIME_ZONE = 'Africa/Johannesburg'
```

## Completed
🏁 [Certificate](https://www.udemy.com/certificate/UC-3e289983-25ff-42ed-8216-0acf05cf9fc1/)