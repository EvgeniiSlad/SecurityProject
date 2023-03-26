from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.
class TimeOfShift(models.Model):
    name = models.CharField(max_length=50,null=True)
    time = models.TimeField(validators=[ValidationError],null=True)

    def __str__(self) :
        return self.name


class Shift(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    data_time = models.DateField(blank=True)
    time_of_shift = models.ForeignKey(TimeOfShift,on_delete=models.CASCADE,null=True)

    def __str__(self) :
        return self.name.last_name
