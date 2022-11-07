from django import forms
from myprojectapp.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            'emp_id': forms.TextInput(attrs={'class':'form-control'}),
            'emp_name': forms.TextInput(attrs={'class':'form-control'}),
            'emp_contact': forms.NumberInput(attrs={'class':'form-control'}),
            'emp_email': forms.EmailInput(attrs={'class':'form-control'}),
            'emp_address': forms.TextInput(attrs={'class': 'form-control'})
        }
