from django.urls import path
from .views import *

urlpatterns = [
    path('restaurant/', views.restaurant_view,name='restaurant'),
    path('contact/', views.contact_us, name='contact-us'),
]