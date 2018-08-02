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
        playlist = []
        followcheck = 0
        following = 0
        followers = 0
        tracks = 0

        response = requests.get('http://127.0.0.1:8000/api/follows/')
        followdata = response.json()
        for i in range(len(followdata)):
            if str(followdata[i]['follower']) == str(usrss) and str(followdata[i]['followed']) == str(usrname):
                followcheck = 1
                break
        if str(usrss) == str(usrname):
            followcheck = -1

        for i in range(len(followdata)):
            if str(followdata[i]['follower']) == str(usrname):
                following += 1
            if str(followdata[i]['followed']) == str(usrname):
                followers += 1
        
        response = requests.get('http://127.0.0.1:8000/api/songs/')
        songdata = response.json()

        for i in range(len(songdata)):
            if str(songdata[i]['owned']) == str(usrname):
                collectiondata.append(songdata[i])
                tracks += 1

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

        response = requests.get('http://127.0.0.1:8000/api/playlists/')
        playlistdata = response.json()

        for i in range(len(playlistdata)):
            if str(playlistdata[i]['owned']) == str(usrname):
                playlist.append(playlistdata[i])
        
        for i in range(len(playlist)):
            playlist[i]['songs'] = []

        response = requests.get('http://127.0.0.1:8000/api/detailpls/')
        detailpldata = response.json()

        for i in range(len(playlist)):
            for j in range(len(detailpldata)):
                if str(playlist[i]['id']) == str(detailpldata[j]['playlist']):
                    for k in range(len(songdata)):
                        if str(detailpldata[j]['song']) == str(songdata[k]['id']):
                            playlist[i]['songs'].append(songdata[k])

        for i in range(len(playlist)):
            for j in range(len(usrdata)):
                if str(usrdata[j]['usrname']) == str(playlist[i]['owned']):
                    playlist[i]['ownedname'] = usrdata[j]['name']

        return render(request, 'profile.html', { 
            'currusr': currusr,
            'watchingusr': watchingusr,
            'collectiondata': collectiondata,
            'playlist': playlist,
            'followcheck': followcheck,
            'following': following,
            'followers': followers,
            'tracks': tracks
            })