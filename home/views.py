from django.shortcuts import render

# Create your views here.

def restaurant_view(request):
    context = {
        'title':'Our Restaurant',
        'description':'Welcome to our exquisite restaurant where culinary artistry meets warm hospitality...',
        'cuisine':'We specialize in authentic Asian cuisine',
        'atmosphere':'Enjoy your meal in our elegantly designed space...'
    }
    return render(request, 'home/restaurant.html', context)

def home_view(request):
    restaurant = Restaurant.objects.first()
    context = {
        'restaurant_name': restaurant.name if restaurant else "Our Restaurant"
    }
    return render(request, 'home/index.html', context)