from django.db import models
# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=11)
    profile_url = models.URLField()


class Vehicle(models.Model):
    license_plate = models.CharField(max_length=10)  # max allowed is 7.
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=15)
    capacity = models.PositiveSmallIntegerField()  # needs to be checked for zero
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Ride(models.Model):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
    )
    passengers = models.ManyToManyField(User)
    destination = models.CharField(max_length=50)
    start = models.CharField(max_length=50)
    # 2008/11/14/13 == 1pm on 11/14/2008
    depart_time = models.CharField(max_length=13)
    seats_offered = models.PositiveSmallIntegerField()  # needs to be checked for zero
    price = models.PositiveSmallIntegerField()
