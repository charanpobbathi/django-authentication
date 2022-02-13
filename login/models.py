from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.username