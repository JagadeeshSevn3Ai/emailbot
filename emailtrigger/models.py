from django.db import models

# Create your models here.

class Botfiles(models.Model):
    Botfile = models.FileField(upload_to='static/document/')