from django.db import models
from django.utils import timezone
from datetime import date



class FoodOrder(models.Model):
    order_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    persons = models.PositiveIntegerField()
    booking_date = models.CharField(max_length=20)  # e.g., '2025-04-06' or '6th April'
    booking_time = models.CharField(max_length=20)  # e.g., '7 PM' or '19:00'
    order = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.order_no} - {self.name}"
