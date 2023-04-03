from django.shortcuts import render
from shifts.models import *
from django.contrib.auth.models import User
from accounts.models import Employee
from django.views.generic import  FormView, UpdateView, DeleteView, ListView ,DetailView
# Create your views here.

def salarys(request):
    employees = Employee.objects.all().order_by('shift')
    context = {
        'employees': employees,
    }
    return render(request, 'salary/salarys.html', context)


class SalaryDetalView(DetailView):
    template_name = 'salary/salary.html'
    model = Employee
    context_object_name = 'salary'
