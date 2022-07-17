from django.contrib import admin

from employees.models import Employee, Position

# Register your models here.
admin.site.register(Position)
admin.site.register(Employee)
