from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.utils import timezone


class UserManagerWrapper(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserBase(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField("email", unique=True, db_index=True)
    first_name = models.CharField("first_name", max_length=120, null=True,
                                  blank=True)
    last_name = models.CharField("last_name", max_length=120, null=True,
                                 blank=True)
    date_joined = models.DateTimeField("data_joined", default=timezone.now)
    is_staff = models.BooleanField(default=False)

    objects = UserManagerWrapper()

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def get_full_name(self):
        fullname = self.email
        return fullname

    def get_short_name(self):
        return self.first_name

