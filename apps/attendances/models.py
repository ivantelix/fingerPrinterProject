from django.db import models
from apps.employees.models import Employee

class Attendance(models.Model):
    TYPE_CHOICES = (
        ('in', 'Entrada'),
        ('out', 'Salida')
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    note = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)