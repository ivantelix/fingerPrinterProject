from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Employee, AttendanceRecord
from .forms import EmployeeCreationForm, AttendanceForm, ClockInForm, ClockOutForm

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'attendance/employee_list.html', {'employees': employees})

@login_required
def attendance_records(request):
    records = AttendanceRecord.objects.all().order_by('-check_in')
    return render(request, 'attendance/records.html', {'records': records})

def clock_in(request):
    if request.method == 'POST':
        form = ClockInForm(request.POST)
        if form.is_valid():
            try:
                employee = Employee.objects.get(identification=form.cleaned_data['identification'])
                AttendanceRecord.objects.create(employee=employee, check_in=timezone.now())
                return render(request, 'attendance/clock_success.html', {
                    'action': 'in',
                    'employee': employee
                })
            except Employee.DoesNotExist:
                form.add_error('identification', 'Employee not found')
    else:
        form = ClockInForm()
    
    return render(request, 'attendance/clock_in.html', {'form': form})

def clock_out(request):
    if request.method == 'POST':
        form = ClockOutForm(request.POST)
        if form.is_valid():
            try:
                employee = Employee.objects.get(identification=form.cleaned_data['identification'])
                # Find the latest check-in without check-out
                record = AttendanceRecord.objects.filter(
                    employee=employee,
                    check_out__isnull=True
                ).latest('check_in')
                record.check_out = timezone.now()
                record.save()
                return render(request, 'attendance/clock_success.html', {
                    'action': 'out',
                    'employee': employee
                })
            except Employee.DoesNotExist:
                form.add_error('identification', 'Employee not found')
            except AttendanceRecord.DoesNotExist:
                form.add_error('identification', 'No active check-in found')
    else:
        form = ClockOutForm()
    
    return render(request, 'attendance/clock_out.html', {'form': form})

@login_required
def employee_attendance(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    records = AttendanceRecord.objects.filter(employee=employee).order_by('-check_in')
    return render(request, 'attendance/employee_attendance.html', {
        'employee': employee,
        'records': records
    })