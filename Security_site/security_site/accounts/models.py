from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to= 'photos/%Y/%m/%d/',default=None)
    email = models.EmailField()
    phone_number = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_absolute_url(self):
        return reverse('salary_detail', args=[str(self.pk)])



# class CustomUser(AbstractUser):
#     phone_number = models.CharField(max_length=20)

#     def __str__(self):
#         return self.last_name
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'
    


