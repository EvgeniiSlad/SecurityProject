from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from accounts.models import *
import requests
# Create your views here.


def homepage(request):
    api_url = 'https://api.open-meteo.com/v1/forecast'
    params = {
        'latitude': 32.08, 
        'longitude': 34.78, 
        'current_weather': 'true', 
        'hourly': 'temperature_2m,relativehumidity_2m,windspeed_10m',
    }
    response = requests.get(api_url, params=params)

    data = response.json()

    if 'current_weather' in data:
        current_weather = data['current_weather']
    else:
        current_weather = {}

    current_temp = current_weather.get('temperature', 'N/A')
    current_humidity = data.get('hourly', {}).get('relativehumidity_2m', [])[0]
    current_wind_speed = current_weather.get('windspeed', 'N/A')

    hourly_data = data.get('hourly', {})
    hourly_times = hourly_data.get('time', [])
    hourly_temperatures = hourly_data.get('temperature_2m', [])
    hourly_humidities = hourly_data.get('relativehumidity_2m', [])
    hourly_wind_speeds = hourly_data.get('windspeed_10m', [])

    context = {
        'current_temp': current_temp,
        'current_humidity': int(current_humidity) if current_humidity else 'N/A',
        'current_wind_speed': current_wind_speed,
        'hourly_times': hourly_times,
        'hourly_temperatures': hourly_temperatures,
        'hourly_humidities': hourly_humidities,
        'hourly_wind_speeds': hourly_wind_speeds,
    }
    return render(request, 'home.html', context)


def add_user(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('add_user')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('add_user')
        else:
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name,phone_number=phone_number)
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('add_user')
  else:
    return render(request, 'accounts/add_user.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      
        auth.login(request, user)
        messages.success(request, 'You are now logged in')
        return redirect('home')
    else:
        messages.error(request, 'Invalid credentials')
        return redirect('login')
  else:
    return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return render(request,'accounts/login.html')


def profile_view(request):
   employees = Employee.objects.all()
   context = {
      'employees': employees
   }
   return render(request,'accounts/profile.html',context)