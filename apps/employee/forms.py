from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Employee, Position, AttendanceRecord

class EmployeeCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=20)
    identification = forms.CharField(max_length=20)
    
    class Meta:
        model = Employee
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'identification', 'position')

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = AttendanceRecord
        fields = ('check_in', 'check_out', 'notes')
        widgets = {
            'check_in': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'check_out': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ClockInForm(forms.Form):
    identification = forms.CharField(max_length=20, label="ID Number")

class ClockOutForm(forms.Form):
    identification = forms.CharField(max_length=20, label="ID Number")