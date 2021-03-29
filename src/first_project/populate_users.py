import django
import random
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

django.setup()

from first_app.models import User
from faker import Faker


fakegen = Faker()


def populate(num=5):
    for entry in range(num):

        u_object = {
            'first_name': fakegen.first_name(),
            'last_name': fakegen.last_name(),
            'email': fakegen.email()
        }

        user = User.objects.get_or_create(**u_object)


if __name__ == '__main__':
    print('Populating Users!')
    populate(20)
    print('Populating Users complete!')
