from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.utils import timezone


class UserBase(AbstractBaseUser):

    email = models.EmailField("email", unique=True, db_index=True)
    first_name = models.CharField("first_name", max_length=120)
    last_name = models.CharField("last_name", max_length=120)
    date_joined = models.DateTimeField("data_joined", default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
