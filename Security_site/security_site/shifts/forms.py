from django import forms
from .models import *




class AddShiftForm(forms.ModelForm):
    # date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    class Meta:
        model = Shift
        fields = ('__all__')

