from django.db import models
from accounts.models import * 

class Stadium(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    cost = models.IntegerField()
    image = models.ImageField(upload_to='media/stadium_images/')
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    booking_untill = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class Bookings(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium,on_delete=models.CASCADE)
    booking_time=models.DateTimeField()
    is_cancelled = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user
    
