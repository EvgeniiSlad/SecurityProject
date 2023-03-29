from django.shortcuts import render
from .models import *
from .forms import AddShiftForm
from django.views.generic import  FormView, UpdateView, DeleteView, ListView ,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy



class ShiftsListView(LoginRequiredMixin,ListView):
    template_name = 'shifts/shifts.html'
    model = Shift
    context_object_name = 'shifts'


class ShiftDetalView(DetailView):
    template_name = 'shifts/shift.html'
    model = Shift
    context_object_name = 'shift'

class addShift(LoginRequiredMixin,FormView):
    form_class = AddShiftForm
    template_name = 'shifts/add_shifts.html'
    success_url = reverse_lazy('shifts')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    




