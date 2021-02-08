from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import *
import time

# Create your views here.


async def index(response):
    return render(response, "MySite/base.html")


def orders(response):
    return render(response, "MySite/orders.html")


def m404(request, exception):
    return render(request, "MySite/404.html")


def registration(response):
    return render(response, "MySite/registration.html")
