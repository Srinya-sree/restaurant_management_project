from django.urls import path
from .views import *

urlpatterns = [
    path('',views.home_view, name='home'),
    path('about/',views.about_view,name='about'),   
]