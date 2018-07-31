from django.shortcuts import render
from django.http import JsonResponse
import requests

def index(request):
    usrss = ''
    if request.session.get('usrss'):
        usrss = request.session.get('usrss')
    if(usrss == ''): return render(request, 'index.html')
    else:
        currusr = {}
        followingusr = []
        streamdata = []
        collectiondata = []

        response = requests.get('http://127.0.0.1:8000/api/follows/')
        followdata = response.json()
        for i in range(len(followdata)):
            if str(followdata[i]['follower']) == str(usrss):
                followingusr.append(followdata[i]['followed'])
        
        response = requests.get('http://127.0.0.1:8000/api/songs/')
        songdata = response.json()

        for i in range(len(followingusr)):
            for j in range(len(songdata)):
                if str(songdata[j]['owned']) == str(followingusr[i]):
                    streamdata.append(songdata[j])

        for i in range(len(songdata)):
            if str(songdata[i]['owned']) == str(usrss):
                collectiondata.append(songdata[i])

        response = requests.get('http://127.0.0.1:8000/api/users/')
        usrdata = response.json()
        for i in range(len(usrdata)):
            if str(usrdata[i]['usrname']) == str(usrss):
                currusr = usrdata[i]
                break

        for i in range(len(streamdata)):
            for j in range(len(usrdata)):
                if str(usrdata[j]['usrname']) == str(streamdata[i]['owned']):
                    streamdata[i]['ownedname'] = usrdata[j]['name']
        
        for i in range(len(collectiondata)):
            for j in range(len(usrdata)):
                if str(usrdata[j]['usrname']) == str(collectiondata[i]['owned']):
                    collectiondata[i]['ownedname'] = usrdata[j]['name']

        return render(request, 'home.html', { 
            'currusr': currusr,
            'streamdata': streamdata,
            'collectiondata': collectiondata,
            })

def signin(request):
    data = {
        'is_success': '',
    }
    usrss = request.GET.get('usrss', None)
    if usrss:
        request.session['usrss'] = str(usrss)
        data['is_success'] = 1
    return JsonResponse(data)

def signout(request):
    data = {
        'is_success': ''
    }
    check = request.GET.get('check', None)
    if(check):
        del request.session['usrss']
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

def profile(request, usrname):
    usrss = ''
    if request.session.get('usrss'):
        usrss = request.session.get('usrss')
    if(usrss == ''): return render(request, 'index.html')
    else:
        currusr = {}
        watchingusr = {}
        collectiondata = []
        followcheck = 0

        response = requests.get('http://127.0.0.1:8000/api/follows/')
        followdata = response.json()
        for i in range(len(followdata)):
            if str(followdata[i]['follower']) == str(usrss) and str(followdata[i]['followed']) == str(usrname):
                followcheck = 1
                break
        
        response = requests.get('http://127.0.0.1:8000/api/songs/')
        songdata = response.json()

        for i in range(len(songdata)):
            if str(songdata[i]['owned']) == str(usrname):
                collectiondata.append(songdata[i])

        response = requests.get('http://127.0.0.1:8000/api/users/')
        usrdata = response.json()

        for i in range(len(usrdata)):
            if str(usrdata[i]['usrname']) == str(usrss):
                currusr = usrdata[i]
                break
        
        for i in range(len(usrdata)):
            if str(usrdata[i]['usrname']) == str(usrname):
                watchingusr = usrdata[i]
                break
        
        for i in range(len(collectiondata)):
            for j in range(len(usrdata)):
                if str(usrdata[j]['usrname']) == str(collectiondata[i]['owned']):
                    collectiondata[i]['ownedname'] = usrdata[j]['name']

        return render(request, 'profile.html', { 
            'currusr': currusr,
            'watchingusr': watchingusr,
            'collectiondata': collectiondata,
            'followcheck': followcheck,
            })