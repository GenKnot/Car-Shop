from django.db import models
from django.utils import timezone


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    car_id = models.IntegerField()
    customer_need = models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.EmailField(max_length=100)
    message = models.TextField(max_length=500, blank=True)
    user_id = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}'s message"
