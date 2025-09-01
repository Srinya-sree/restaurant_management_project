from django.conf import settings
from django.shortcuts import render, redirect
from .forms import Form
form .forms import ContactForm
def home_view(request):
    restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'My Restaurant')
    return render(request, 'home.html',{'restaurant_name': restaurant_name})
def about_view(request):
    return render(request, 'about.html')
def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            form = ContactForm()
    context={
        "form":form,
        "restaurant_address":settings.RESTAURANT_ADDRESS,
        "restaurant_name":settings.RESTAURANT_NAME
    }
    api_url = "http://127.0.0.1:8000/api/menu/"
    return render(request,"home.html",context)
try:
    response = requests.get(api_url)
    menu_items=response.json()
except:
    menu_items=[]
    return render(request,"home.html",{"menu_items":menu_items})
def menu_page(request):
    items = Menu.objects.all()
    return render(request,"menu.html",{"items":items})

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form':form})
