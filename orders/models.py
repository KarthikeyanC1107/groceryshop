from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    items = models.TextField()
    payment_method = models.CharField(max_length=50)
    pickup_time = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order from {self.name} - {self.phone}"
