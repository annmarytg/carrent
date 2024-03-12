
# Register your models here.
from django.contrib import admin
from bookings.models import Booking,BookingItem
# Register your models here.
class  BookingAdmin(admin.ModelAdmin):
    list_filter =[
        "owner",
        "booking_status",
    ]
    search_fields=(
        "owner",
        "id",
    )
admin.site.register(Booking,BookingAdmin)
