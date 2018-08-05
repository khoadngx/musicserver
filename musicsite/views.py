from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests

def index(request):
    # get session
    usrss = ''
    if request.session.get('usrss'):
        usrss = request.session.get('usrss')
    # if there ain't no session redirect to the index page
    if(usrss == ''): return render(request, 'index.html')
    else:
        currusr = {}
        followingusr = []
        streamdata = []
        collectiondata = []
        playlist = []

        # get all users that current user followed
        response = requests.get('http://127.0.0.1:8000/api/follows/')
        followdata = response.json()
        for i in range(len(followdata)):
            if str(followdata[i]['follower']) == str(usrss):
                followingusr.append(followdata[i]['followed'])
        
        response = requests.get('http://127.0.0.1:8000/api/songs/')
        songdata = response.json()

        # streamdata: songs of all users that current user followed
        for i in range(len(followingusr)):
            for j in range(len(songdata)):
                if str(songdata[j]['owned']) == str(followingusr[i]):
                    streamdata.append(songdata[j])

        # collectiondata: all songs of current user
        for i in range(len(songdata)):
            if str(songdata[i]['owned']) == str(usrss):
                collectiondata.append(songdata[i])

        response = requests.get('http://127.0.0.1:8000/api/users/')
        usrdata = response.json()
        # current user info
        for i in range(len(usrdata)):
            if str(usrdata[i]['usrname']) == str(usrss):
                currusr = usrdata[i]
                break

        # name of users own songs in streamdata
        for i in range(len(streamdata)):
            for j in range(len(usrdata)):
                if str(usrdata[j]['usrname']) == str(streamdata[i]['owned']):
                    streamdata[i]['ownedname'] = usrdata[j]['name']
        
        # name of users own songs in collectiondata
        for i in range(len(collectiondata)):
            for j in range(len(usrdata)):
                if str(usrdata[j]['usrname']) == str(collectiondata[i]['owned']):
                    collectiondata[i]['ownedname'] = usrdata[j]['name']
        
        response = requests.get('http://127.0.0.1:8000/api/playlists/')
        playlistdata = response.json()

        # create playlist which include playlist's data of current user
        for i in range(len(playlistdata)):
            if str(playlistdata[i]['owned']) == str(usrss):
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

        # name of users own songs in playlist
        for i in range(len(playlist)):
            for j in range(len(usrdata)):
                if str(usrdata[j]['usrname']) == str(playlist[i]['owned']):
                    playlist[i]['ownedname'] = usrdata[j]['name']

        return render(request, 'home.html', { 
            'currusr': currusr,
            'streamdata': streamdata,
            'collectiondata': collectiondata,
            'playlist': playlist
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
    # get session
    usrss = ''
    if request.session.get('usrss'):
        usrss = request.session.get('usrss')
    # if there ain't no session redirect to the index page
    if(usrss == ''): return render(request, 'index.html')
    else:
        currusr = {}
        watchingusr = {}
        collectiondata = []
        playlist = []
        usrpl = []
        followcheck = 0
        following = 0
        followers = 0
        tracks = 0

        # check current user follow watching user or not
        response = requests.get('http://127.0.0.1:8000/api/follows/')
        followdata = response.json()
        for i in range(len(followdata)):
            if str(followdata[i]['follower']) == str(usrss) and str(followdata[i]['followed']) == str(usrname):
                followcheck = 1
                break

        # if current user visit his/her own profile
        if str(usrss) == str(usrname):
            followcheck = -1

        # quantity of following and followers
        for i in range(len(followdata)):
            if str(followdata[i]['follower']) == str(usrname):
                following += 1
            if str(followdata[i]['followed']) == str(usrname):
                followers += 1
        
        response = requests.get('http://127.0.0.1:8000/api/songs/')
        songdata = response.json()

        # collectiondata: all songs of watching user and quantity of his/her tracks
        for i in range(len(songdata)):
            if str(songdata[i]['owned']) == str(usrname):
                collectiondata.append(songdata[i])
                tracks += 1

        response = requests.get('http://127.0.0.1:8000/api/users/')
        usrdata = response.json()

        # current user info
        for i in range(len(usrdata)):
            if str(usrdata[i]['usrname']) == str(usrss):
                currusr = usrdata[i]
                break
        
        # watching user info
        for i in range(len(usrdata)):
            if str(usrdata[i]['usrname']) == str(usrname):
                watchingusr = usrdata[i]
                break
        
        # name of users own songs in collectiondata
        for i in range(len(collectiondata)):
            for j in range(len(usrdata)):
                if str(usrdata[j]['usrname']) == str(collectiondata[i]['owned']):
                    collectiondata[i]['ownedname'] = usrdata[j]['name']

        response = requests.get('http://127.0.0.1:8000/api/playlists/')
        playlistdata = response.json()

        # create playlist which include playlist's data of watching user
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

        # name of users own songs in playlist
        for i in range(len(playlist)):
            for j in range(len(usrdata)):
                if str(usrdata[j]['usrname']) == str(playlist[i]['owned']):
                    playlist[i]['ownedname'] = usrdata[j]['name']

        return render(request, 'profile.html', { 
            'currusr': currusr,
            'watchingusr': watchingusr,
            'collectiondata': collectiondata,
            'playlist': playlist,
            'usrpl': usrpl,
            'followcheck': followcheck,
            'following': following,
            'followers': followers,
            'tracks': tracks
            })

def search(request, keyword):
    # get session
    usrss = ''
    if request.session.get('usrss'):
        usrss = request.session.get('usrss')
    # if there ain't no session redirect to the index page
    if(usrss == ''): return render(request, 'index.html')
    else:
        usrsr = []
        songsr = []
        plsr = []

        # users search
        response = requests.get('http://127.0.0.1:8000/api/users/?search=' + str(keyword))
        usrdata = response.json()

        for i in range(len(usrdata)):
            usrsr.append(usrdata[i])

        # songs search
        response = requests.get('http://127.0.0.1:8000/api/songs/?search=' + str(keyword))
        songdata = response.json()

        for i in range(len(songdata)):
            songsr.append(songdata[i])

        # playlists search
        response = requests.get('http://127.0.0.1:8000/api/playlists/?search=' + str(keyword))
        playlistdata = response.json()

        for i in range(len(playlistdata)):
            plsr.append(playlistdata[i])

        return render(request, 'search.html', { 
                'usrsr': usrsr,
                'songsr': songsr,
                'plsr': plsr,
                })