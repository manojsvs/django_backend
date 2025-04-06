from django.db import models

class BikeOrder(models.Model):
    sno = models.AutoField(primary_key=True)
    order_no = models.CharField(max_length=20)
    model_no = models.CharField(max_length=50)
    bike_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)  # NEW

    def __str__(self):
        return f"{self.order_no} - {self.bike_name}"
