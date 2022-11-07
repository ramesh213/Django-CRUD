from django.db import models


# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=100)
    emp_contact = models.CharField(max_length=15)
    emp_email = models.EmailField()
    emp_address = models.CharField(max_length=150)

    # This class creates table name 'employee' in database
    class Meta:
        db_table = "employee"

    # This method returns  employee name instead of 'object' in admin panel
    # def __str__(self):
    #     return self.emp_name
