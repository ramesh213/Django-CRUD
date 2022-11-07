from django.shortcuts import render, redirect
from myprojectapp.form import EmployeeForm
from myprojectapp.models import Employee
from django.contrib import messages


# Create your views here.
def create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid:
            try:
                form.save()
                messages.success(request,'Record Successfully Added !!!')
                return redirect('/create')
            except:
                pass
    else:
        form = EmployeeForm()
        return render(request, "index.html ", {'form': form})


def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {'employees': employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, "edit.html", {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        messages.success(request,'Record updated successfully !!!')
        return redirect('/show')
    else:
        return render(request,"edit.html", {'employee': employee})


def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    messages.success(request,'Record Deleted Successfully !!!')
    return redirect('/show')
