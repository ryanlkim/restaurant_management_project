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

def contact_us(request):
    #Hardcoded contact information
    contact_info = {
        'title': 'Contact us',
        'address' : '123 Restaurant Street, Foodville, FV 12345',
        'phone' : '(555) 123-4567',
        'email' : 'info@restaurantmanagement.com',
        'hours' : {
            'weekdays' : '9:00 AM - 10:00 PM',
            'weekends' : '10:00 AM- 11:00PM'
        }
    }
    return render(request, 'home/contact.html', contact_info)

def home(request):
    context = {
        'phone_number': settings.RESTARUANT_INFO['PHONE'],
    }
    return render(request, 'home/index.html', context)