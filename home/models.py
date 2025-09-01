from django.db import models
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
class MenuItem(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to="menu_images/",blank = True,null=True)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    submitted_at = models.DateTimeField(auto_now_add=True)
     def __str__(self):
        return self.name
        return f"{self.name} - ${self.price}"
        return f"{self.name}-{self.email}"

class RestaurantLocation(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.address},{self.city},{self.state}{self.zip_code}"

