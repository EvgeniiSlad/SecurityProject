from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.forms.fields import DateField
from accounts.models import Employee
from django.db.models.functions import TruncDate
# Create your models here.
class TimeOfShift(models.Model):
    name = models.CharField(max_length=50,null=True)
    time = models.TimeField(validators=[ValidationError],null=True)
    price = models.IntegerField(null=True)

    def __str__(self) :
        return self.name


class Shift(models.Model):
    name = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    data_time = models.DateField(null=True)
    time_of_shift = models.ForeignKey(TimeOfShift,on_delete=models.CASCADE, null=True)

    def __str__(self) :
        return f'{self.name.first_name} {self.name.last_name}'

