from django.contrib import admin
from django.urls import path
from accounts.views import *
from shifts.views import *
from salary.views import*
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage, name='home'),
    path('login/',login, name='login'),
    path('logout/',logout, name='logout'),
    path('profile/',profile_view,name='profile'),
    path('add_user/',add_user, name='add_user') ,
    path('add_shifts/',addShift.as_view(),name='add_shifts'),
    path('shifts/',ShiftsListView.as_view(),name='shifts'),
    path('shift/<int:pk>',ShiftDetalView.as_view(),name='shift'),
    path('shifts_for/',count_shist,name='shifts_for'),
    path('salarys/',salarys,name='salarys'),
    path('salary/<int:pk>',SalaryDetalView.as_view(),name='salary'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

