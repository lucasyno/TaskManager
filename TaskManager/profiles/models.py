from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models


class Profile(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()

    objects = UserManager()
    USERNAME_FIELD = 'username'
