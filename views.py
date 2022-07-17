from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

# deal with get and post for insert and update operation
def employee_form(request, id=0):
    if request.method == 'GET':
        # for insert operation we'll set an empty form
        if id == 0 :
            form = EmployeeForm()
        # for update operation populate the form with corresponding form details
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance = employee)
        return render(request, "employees/employee_form.html", {'form':form})
    else:
        if id==0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form=EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/list')
    

# Retrieve information stored in the database
def employee_list(request):
    context = {
        'employee_list': Employee.objects.all()
    }
    return render(request, "employees/employee_list.html", context)

# delete operation
def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list')
