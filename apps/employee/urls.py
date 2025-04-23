from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('attendance/', views.attendance_records, name='attendance_records'),
    path('clock-in/', views.clock_in, name='clock_in'),
    path('clock-out/', views.clock_out, name='clock_out'),
    path(
            'employee/<int:employee_id>/attendance/',
            views.employee_attendance,
            name='employee_attendance'
        ),
]
