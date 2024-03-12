from django.shortcuts import render,redirect
from .models import Booking,BookingItem
from cars.models import Car
from django.contrib import messages
from  django.contrib.auth.decorators import login_required

# Create your views here.
def show_cart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj,created=Booking.objects.get_or_create(
           owner=customer,
           booking_status=Booking.CART_STAGE
        )
    context={'cart':cart_obj}
    return render(request, 'cart.html',context)
def remove_item_from_cart(request,pk):
    item=BookingItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')

def checkout_cart(request):
    if request.POST:
        try:
            user=request.user
            customer=user.customer_profile
            total=float(request.POST.get('total'))
            booking_obj=Booking.objects.get(
            owner=customer,
            booking_status=Booking.CART_STAGE
            )
            if booking_obj:
                booking_obj.booking_status=Booking.BOOKING_CONFIRMED
                booking_obj.total_price=total
                booking_obj.save()
                status_message="your booking is processed."
                messages.success(request,status_message)
            else:
                status_message="unable to processed."
                messages.error(request,status_message)

        except Exception  as e:
            status_message="unable to processed."
            messages.error(request,status_message)
    return redirect('cart')
        
@login_required(login_url='account')
def show_bookings(request):
    user=request.user
    customer=user.customer_profile
    all_bookings=Booking.objects.filter(owner=customer).exclude(booking_status=Booking.CART_STAGE)
    context={'bookings':all_bookings}
    
    return render(request, 'bookings.html',context)

def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        days=int(request.POST.get('days'))
        car_id=request.POST.get('car_id')
        cart_obj,created=Booking.objects.get_or_create(
           owner=customer,
           booking_status=Booking.CART_STAGE
        )
        car=Car.objects.get(pk=car_id)
        booking_item,created=BookingItem.objects.get_or_create(
            car=car,
            owner=cart_obj,
            days=days
        )
        if created:
            booking_item.days=days
            booking_item.save()
        else:
            booking_item.days=booking_item.days+days
            booking_item.save()
            
    return redirect('cart')
