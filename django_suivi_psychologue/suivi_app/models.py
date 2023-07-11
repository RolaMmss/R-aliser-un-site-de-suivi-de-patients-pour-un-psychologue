from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils import timezone

class User(AbstractUser):
    pass

class Psychologue(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    # Autres champs

class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)
    # Autres champs

class Texte(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # Autres champs

class Evaluation(models.Model):
    texte = models.ForeignKey(Texte, on_delete=models.CASCADE)
    emotion = models.CharField(max_length=100)
    confidence = models.FloatField()
    # Autres champs
