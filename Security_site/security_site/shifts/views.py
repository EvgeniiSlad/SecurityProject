from django.shortcuts import render
from .models import *
from .forms import AddShiftForm
from django.views.generic import  FormView, UpdateView, DeleteView, ListView ,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Sum
from datetime import datetime, timedelta



class ShiftsListView(LoginRequiredMixin,ListView):
    template_name = 'shifts/shifts.html'
    model = Shift
    context_object_name = 'shifts'


class ShiftDetalView(DetailView):
    template_name = 'shifts/shift.html'
    model = Shift
    context_object_name = 'shift'


def count_shist(request):
    employee_last_name = request.user.last_name
    shifts = Shift.objects.filter(name__last_name=employee_last_name)
    sum_salary = shifts.aggregate(total_salary=Sum('time_of_shift__price'))
    context ={
        'shifts': shifts,
        'sum_salary': sum_salary
    }
    return render(request,'shifts/shifts_for.html',context)


class addShift(LoginRequiredMixin,FormView):
    form_class = AddShiftForm
    template_name = 'shifts/add_shifts.html'
    success_url = reverse_lazy('shifts')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class addTimeOfShift(LoginRequiredMixin,FormView):
    form_class = TimeOfShift
    template_name = 'shifts/add_time.html'
    success_url = reverse_lazy('add_time')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


    




