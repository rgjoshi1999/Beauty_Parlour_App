from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)


'''
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
'''

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    service = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    confirmed = models.BooleanField(default=False)

class Feedback(models.Model):
    username = models.CharField(max_length=30)
    created_data = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField()


