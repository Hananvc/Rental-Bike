from django import forms 

from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields= '__all__'

        widgets ={
            'Booking_date':DateInput(),
        }

        labels = {
            'Name' :'Name: ',
            'Phone' : 'Phone: ',
            'Email' : 'E-mail: ',
            'Model' :'Model: ',
            
            
        }
    






