from django.db import models

# Contains members who attended a class by signing in
class Attended_class(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20)
