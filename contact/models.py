from django.db import models

# Create your models here.
class Message(models.Model):
    email = models.EmailField()
    subject = models.TextField()


class Project(models.Model):
    name = models.CharField(max_length=50)
    tel_number = models.CharField(max_length=15)
    email = models.EmailField()
    idea = models.TextField()

