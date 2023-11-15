from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json

# Create your views here.
def home(request):
    employees = Employee.objects.all()
    context = {'employee': employees}
    return render(request, 'vnany/home.html')