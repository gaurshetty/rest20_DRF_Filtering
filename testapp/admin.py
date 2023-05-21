from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'no', 'name', 'salary', 'address']


admin.site.register(Employee, EmployeeAdmin)
