from django.shortcuts import render
from django.http import JsonResponse
import requests

def index(request):
    usrname = ''
    usrss = ''
    currentusr = {}
    if request.session.get('usrname'):
        usrname = request.session.get('usrname')
        usrss = request.session.get('usrss')
    response = requests.get('http://127.0.0.1:8000/api/users/')
    usrdata = response.json()
    for i in range(len(usrdata)):
        if str(usrdata[i]['usrname']) == str(usrname):
            currentusr = usrdata[i]
    return render(request, 'index.html', { 
        'usrss': usrss, 
        'usrname': usrss,
        'currentusr': currentusr,
        })

def signin(request):
    data = {
        'is_success': '',
    }
    usrss = request.GET.get('usrss', None)
    usrname = request.GET.get('usrname', None)
    if usrname:
        request.session['usrss'] = str(usrss)
        request.session['usrname'] = str(usrname)
        data['is_success'] = 1
    return JsonResponse(data)

def signout(request):
    data = {
        'is_success': ''
    }
    check = request.GET.get('check', None)
    if(check):
        del request.session['usrss']
        del request.session['usrname']
        data['is_success'] = 1
    return JsonResponse(data)

def validate_usrname(request):
    data = {
        'is_taken': ''
    }
    usrname = request.GET.get('usrname', None)
    response = requests.get('http://127.0.0.1:8000/api/users/')
    usrdata = response.json()
    for i in range(len(usrdata)):
        if str(usrdata[i]['usrname']) == str(usrname):
            data['is_taken'] = 1
            break
    return JsonResponse(data)

def home(request):
    response = requests.get('http://127.0.0.1:8000/api/songs/')
    songdata = response.json()
    return render(request, 'home.html', { 'data': songdata })
