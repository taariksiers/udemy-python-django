from django.contrib.auth.models import PermissionsMixin, User as AuthUser
from django.db import models


class User(AuthUser, PermissionsMixin):

    def __str__(self):
        return f"@{self.username}"
