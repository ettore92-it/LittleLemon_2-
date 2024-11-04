from django.shortcuts import render
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# Class for handling list and creation of menu items
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Class for handling retrieval, update, and deletion of a single menu item
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Fetch all objects from the Booking model
    serializer_class = BookingSerializer  # Set serializer to BookingSerializer
