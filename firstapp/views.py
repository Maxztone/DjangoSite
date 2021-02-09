from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import *
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from firstapp.models import Dishes
from firstapp.serializers import DishesSerializer
from rest_framework import filters
# Create your views here.


def index(response):
    return render(response, "MySite/base.html")


def orders(response):
    return render(response, "MySite/orders.html")


def m404(request, exception):
    return render(request, "MySite/404.html")


def registration(response):
    return render(response, "MySite/registration.html")


# Future page. Should change render value when you will create a restaurant page.
def restaurant(response):
    return render(response, "MySite/404.html")


class DishesViewSet(ModelViewSet):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer
