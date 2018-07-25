from django.shortcuts import render
from django.http import JsonResponse
import requests

def home(request):
    response = requests.get('http://127.0.0.1:8000/api/users/')
    usrdata = response.json()
    return render(request, 'home.html', { 'data': usrdata })