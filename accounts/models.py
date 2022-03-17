from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)    # age bu foydalanuvchidan yoshini ham kiritishini soraydi
    manzil = models.CharField(max_length=100, null=True, blank=True)

