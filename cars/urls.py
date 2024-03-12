from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.index,name='home'),
    path('car_list', views.list_cars,name='list_car'),
    path('car_details/<pk>', views.detail_cars,name='detail_car'),


    
]