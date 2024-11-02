from django.db import models
from django.conf import settings

# Create your models here.

""""
class Address(models.Model):

    street_address = models.CharField("Street Address", max_length=255)
    city = models.CharField("city", max_length=255)
    state = models.CharField("state", max_length=255)
    zipcode = models.IntegerField("zipcode")

"""


class Farmer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="farmer", on_delete=models.CASCADE)
    name = models.CharField("Farmer Name", max_length=255)
    phone_number = models.IntegerField("Phone Number")
    email = models.CharField("Email", max_length=255)

    def __str__(self):
        return self.name




class Farm(models.Model):

    name = models.CharField("Farm Name", max_length=255)
    farmer = models.ForeignKey(Farmer, related_name="farmers", on_delete=models.CASCADE)
    street_address = models.CharField("Street Address", max_length=255, default='800 N Columbia Ave')
    city = models.CharField("city", max_length=255, default='Seward')
    state = models.CharField("state", max_length=255, default='Nebraska')
    zipcode = models.IntegerField("zipcode", default='12345')


    def __str__(self):
        return self.name

class Pig(models.Model):

    name = models.CharField("Pig Tag Number", max_length=255)
    temperature = models.FloatField("Temperature")
    weight = models.IntegerField("Weight")
    birthday = models.DateField("Birthday")
    farm = models.ForeignKey(Farm, related_name="farms", on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Immunization(models.Model):

    name = models.CharField("Immunization name", max_length=255)
    date_given = models.DateField("Date immunization given")
    reason = models.CharField("Reason for immunization given", max_length=255)
    pig = models.ForeignKey(Pig, related_name="pigs", on_delete=models.CASCADE, default='-1')

    def __str__(self):
        return self.name


class Past_Farm_Record(models.Model):

    date_arrived = models.DateField("Date Arrived")
#    date_departed = models.DateField("Date Departed")
    pig = models.ForeignKey(Pig, related_name="past_pig_records", on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, related_name="past_farm_records", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Past Farm Record"
        verbose_name_plural = "Past Farm Records"

    def __str__(self):
        return "Past Farm Record"





    
