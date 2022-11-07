from django.contrib import admin
from myprojectapp.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'emp_id', 'emp_name', 'emp_contact', 'emp_email', 'emp_address')


# Register your models here.
admin.site.register(Employee, EmployeeAdmin)
