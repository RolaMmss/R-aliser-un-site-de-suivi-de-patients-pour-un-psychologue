from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Classe pour l'utilisateur 
class User(AbstractUser):
    
    class Role(models.TextChoices):
        CLIENT = 'CLIENT'
        ADMIN = 'ADMIN'
    role = models.fields.CharField(choices=Role.choices, max_length=6, default='CLIENT')
    