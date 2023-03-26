from django.contrib import admin
from django.urls import path
from accounts.views import *
from shifts.views import *
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage, name='home'),
    path('login/',login, name='login'),
    path('logout/',logout, name='logout'),
    path('add_user/',add_user, name='add_user') ,
    path('add_shifts/',addShift.as_view(),name='add_shifts'),
    path('shifts/',ShiftsListView.as_view(),name='shifts')
]
