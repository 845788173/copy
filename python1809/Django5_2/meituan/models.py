from django.db import models

# Create your models here.
class User(models.Model):
    u_name = models.CharField(max_length=50)
    u_password = models.CharField(max_length=50)
    u_tel = models.CharField(max_length=20)
