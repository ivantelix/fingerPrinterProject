from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    identification = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"