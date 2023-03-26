from django import forms
from .models import *




class AddShiftForm(forms.ModelForm):

    class Meta:
        model = Shift
        fields = ('__all__')
