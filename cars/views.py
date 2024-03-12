from django.shortcuts import render
from .models import Car
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    featured_cars=Car.objects.order_by('priority')[:4]
    latest_cars=Car.objects.order_by('-id')[:4]
    context={
        'featured_cars':featured_cars,
        'latest_cars':latest_cars
    }
    return render(request,'index.html',context)
def list_cars(request):
    """_summary_
    returns product list page

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    car_list=Car.objects.order_by('priority')
    car_paginator=Paginator(car_list,3)
    car_list=car_paginator.get_page(page)
    context={'cars':car_list}
    return render(request,'cars.html',context)
def detail_cars(request,pk):
    car=Car.objects.get(pk=pk)
    context={'car':car}
    return render(request,'car_details.html',context)