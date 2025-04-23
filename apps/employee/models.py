from django.db import models
from django.contrib.auth.models import AbstractUser


class Department(models.Model):
    name = models.CharField('Departamento', max_length=100)
    description = models.CharField(
        'Descripción',
        max_length=100,
        blank=True,
        null=True
    )


class Position(models.Model):
    name = models.CharField('Puesto', max_length=100)
    description = models.CharField(
        'Descripción',
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Employee(AbstractUser):
    phone = models.CharField(max_length=20)
    identification = models.CharField(max_length=20, unique=True)
    position = models.ForeignKey(
        Position, 
        on_delete=models.SET_NULL,
        null=True
    )

    # Remove unused fields from AbstractUser
    groups = None
    user_permissions = None

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position})"


class AttendanceRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-check_in']

    def duration(self):
        if self.check_out:
            return self.check_out - self.check_in
        return None

    def __str__(self):
        return f"{self.employee} - {self.check_in.date()}"
