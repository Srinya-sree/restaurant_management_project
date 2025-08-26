from django.db import models
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    submitted_at = models.DateTimeField(auto_now_add=True)
     def __str__(self):
        return self.name
        return f"{self.name} - ${self.price}"
        return f"{self.name}-{self.email}"