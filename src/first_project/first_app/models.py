from django.db import models


class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        """
        Meh
        """
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        """
        Meh
        """
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        """
        Meh
        """
        return str(self.date)


class User(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField(max_length=264, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        """
        Meh
        """
        return f'{self.first_name} {self.last_name} - {self.email}'
