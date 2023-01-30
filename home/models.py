from django.db import models

# Create your models here.


class Inventory(models.Model):
    bikes_name=models.CharField(max_length=255)
    bikes_spec=models.CharField(max_length=255)
    bikes_image=models.ImageField(upload_to='bikes')

    def __str__(self):
        return  self.bikes_name + '-  '+self.bikes_spec 


class Booking(models.Model):
    Name=models.CharField(max_length=255)
    Phone=models.CharField(max_length=10)
    Email=models.EmailField()
    Model=models.ForeignKey(Inventory,on_delete=models.CASCADE)
    Booked_on=models.DateField(auto_now=True)
    

