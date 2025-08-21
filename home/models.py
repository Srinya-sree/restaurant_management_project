from django.db import models
from django.contrib.auth.models import User

#creating class Restaurant
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

#creating Menu model
class Menu(models.Model):
    name = models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    def __str__(self):
        return self.name

#creating order model
class Orders(models.Model):
    STATUS_CHOICES=(
        ('PENDING','Pending'),
        ('CONFIRMED','Confirmed'),
        ('DELIVERD','Deliverd'),
        ('CANCELLED','cancelled'),
    )
    customer = models.ForeignKey(User,on_delete=models.CASCADE,related_name="orders")
    items=models.ManyToManyField(Menu,related_name="orders")
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='PENDING')
    created_at=models.DateTimeField(auto_now_add=True)#timesamp
    def __str__(self):
        return f"Order#{self.id} by {self.customer.username}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=15,blank=True,null=True)
    def __str__(self):
        return self.user.username