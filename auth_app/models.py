from django.db import models
from django.contrib.auth.models import (AbstractUser, AbstractBaseUser,PermissionsMixin)
from django.contrib.auth.base_user import BaseUserManager


class AppUserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('email is required')
        if not password:
            raise ValueError('passoword is required')
        user: AppUser = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email=email, password=password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class AppUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AppUserManager()
