from unittest.loader import VALID_MODULE_NAME
from django.db import models
import uuid
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, name, email, password=None):
        if not email:
            raise ValueError('Email address is required')

        if not name:
            raise ValueError('Name is required')
        user = self.model(
            name = name,
            email = self.normalize_email(email),
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        if password is None:
            raise TypeError('Superuser require password')
        
        user = self.create_user(email, password)
        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=False)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email
