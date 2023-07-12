from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class home_page(models.Model):
    slug = models.CharField(
        max_length = 100,
        blank =  False,
    )



# class TestModel(models.Model):
#     resultat = models.CharField(max_length=500)
    
    

class Patient(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # Autres champs du patient

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    

class Text(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    content = models.TextField()
    evaluation = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.content[:50]  # Return a truncated version of the content

    class Meta:
        verbose_name_plural = 'Texts'
        
class Emotion(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    evaluation = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.evaluation

    class Meta:
        verbose_name_plural = 'Emotions'