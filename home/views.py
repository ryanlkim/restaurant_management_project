from django.shortcuts import render

# Create your views here.

def resturant_view(request):
    context = {
        'title':'Our Resturant',
        'description':'Welcome to our exquisite resturant where culinary artistry meets warm hospitality...',
        'cuisine':'We specialize in authentic Asian cuisine',
        'atmosphere':'Enjoy your meal in our elegantly designed space...'
    }
    return render(request, 'home/resturant.html', context)

def home_view(request):
    context = {
        'resturant_name':settings.RESTURANT_CONFIG['NAME'],
    }
    return render(request, 'home/index.html', context)