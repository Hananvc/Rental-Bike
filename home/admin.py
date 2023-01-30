from django.contrib import admin


from .models import Booking,Inventory
# Register your models here.


admin.site.register(Inventory)

class BookingAdmin(admin.ModelAdmin):
    list_display=('id' ,'Name' ,'Phone' ,'Email' ,'Model' , 'Booked_on')

admin.site.register(Booking,BookingAdmin)