from django.shortcuts import render, redirect
# from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import json
import datetime
from django.contrib import messages
# from .utils import cartData, guestOrder
from django.contrib.auth import logout as django_logout
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django import forms
from django.conf import settings




def index(request):
    if request.method == "GET":
        context ={"Tittle": "index"}
        return render(request, "index.html", context)

# def newarrival(request):
#     if request.method == "GET":
#         product = Product.objects.all()
#         Men = category.objects.filter(men=True).order_by('Name')
#         Women = category.objects.filter(women=True).order_by('Name')
#         Kids = category.objects.filter(kids=True).order_by('Name')
#         accessories = category.objects.filter(accessories=True).order_by('Name')
#         essential = category.objects.filter(essential=True).order_by('Name')
#     context = {"Tittle": "newarrival", "product": product, "Men": Men, "Women": Women, "Kids": Kids,
#                "accessories": accessories, "essential": essential}
#     return render(request, "new arrival.html", context)