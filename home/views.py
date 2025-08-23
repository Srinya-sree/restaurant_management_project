from django.conf import settings
from django.shortcuts import render

def home_view(request):
    restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'My Restaurant')
    return render(request, 'home.html',{'restaurant_name': restaurant_name})
def about_view(request):
    return render(request, 'about.html')
def home(request):
    api_url = "http://127.0.0.1:8000/api/menu/"
try:
    response = requests.get(api_url)
    menu_items=response.json()
except:
    menu_items=[]
    return render(request,"home.html",{"menu_items":menu_items})