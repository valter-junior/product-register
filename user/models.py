from django.db import models
import uuid
# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=False)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email
