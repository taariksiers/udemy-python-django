import django
import random
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

django.setup()

from first_app.models import AccessRecord, Topic, Webpage
from faker import Faker


fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(num=5):
    for entry in range(num):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print('Populating script!')
    populate(20)
    print('Populating complete!')
