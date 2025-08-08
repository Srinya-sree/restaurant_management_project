from django.conf import settings
from django.shortcuts import render

def home_view(request):
    restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'My Restaurant')
    return render(request, 'home.html',{'restaurant_name': restaurant_name})