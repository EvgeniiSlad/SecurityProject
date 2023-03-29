from django.shortcuts import render
from shifts.models import *
from django.contrib.auth.models import User
from accounts.models import Employee
# Create your views here.

def salary(request):
    users = Employee.objects.all().order_by('shift')
    context = {
        'users': users,
    }
    return render(request, 'salary/salary.html', context)
