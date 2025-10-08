from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .models import MenuItem, BookingItem
from .serializers import MenuItemSerializer, BookingItemSerializer, BookingSerializer, UserSerializer

# Create your views here.
# def sayHello(request):
#     return HttpResponse('Hello World')


# def index(request):
#     return render(request, 'index2.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView,
                         generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = BookingItem.objects.all()
    serializer_class = BookingSerializer


# class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all() 
#    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated] 