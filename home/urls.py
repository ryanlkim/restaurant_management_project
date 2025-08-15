from django.urls import path
from .views import *

urlpatterns = [
    path('resturant/', views.resturant_view,name='resturant')
]