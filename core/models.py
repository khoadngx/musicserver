from django.db import models

class User(models.Model):
    usrname = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    passwd = models.CharField(max_length=30)
    dob = models.DateField()
    ava = models.CharField(max_length=200, blank=True, default='')
    following = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)

class Song(models.Model):
    name = models.CharField(max_length=100)
    owned = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now=True)
    plays = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)