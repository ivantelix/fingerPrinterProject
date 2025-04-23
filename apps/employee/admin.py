from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Position, Employee, AttendanceRecord

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'position', 'identification')
    list_filter = ('position',)
    search_fields = ('first_name', 'last_name', 'email', 'identification')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone', 'identification', 'position')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone', 'identification', 'position'),
        }),
    )

@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('employee', 'check_in', 'check_out', 'duration')
    list_filter = ('employee',)
    search_fields = ('employee__first_name', 'employee__last_name')
    date_hierarchy = 'check_in'