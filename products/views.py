from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def menu_items_list(request):
        # Hardcoded list of menu items (will be replaced with DB query later)
        menu_items = [
            {'name': 'Margherita Pizza', 'price': 12.99, 'description': 'Classic pizza with tomato sauce and mozzarella'},
            {'name': 'Spaghetti Carbonara', 'price': 14.99, 'description': 'Pasta with creamy egg sauce and pancetta'},
            {'name': 'Caesar Salad', 'price': 8.99, 'description': 'Romaine lettuce with Caesar dressing and croutons'},
            {'name': 'Tiramisu', 'price': 6.99, 'description': 'Classic Italian dessert with coffee flavor'},
        ]

        context = {
            'menu_items': menu_items,
            'title': 'Our Menu'
        }
        return render(request, 'products/menu_items.html', context)