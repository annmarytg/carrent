from django.db import models
from customers.models import Customer
from cars.models import Car

# Create your models here.
class Booking(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE=0
    BOOKING_CONFIRMED=1
    BOOKING_PROCESSED=2
    BOOKING_DELIVERED=3
    BOOKING_REJECTED=4
    STATUS_CHOICE=((BOOKING_PROCESSED,"BOOKING_PROCESSED"),
                   (BOOKING_DELIVERED,"BOOKING_DELIVERED"),
                   (BOOKING_REJECTED,"BOOKING_REJECTED"),
                
                   )
    booking_status=models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    total_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    owner=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,related_name='bookings')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:

        return "booking-{}-{}".format(self.id,self.owner.name)

class BookingItem(models.Model):
    car=models.ForeignKey(Car,related_name='added_carts',on_delete=models.SET_NULL,null=True)
    days = models.IntegerField(default=1)
    owner=models.ForeignKey(Booking,on_delete=models.CASCADE,related_name='added_items')

