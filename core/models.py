from django.db import models

class User(models.Model):
    usrname = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100, null=False)
    passwd = models.CharField(max_length=30, null=False)
    dob = models.DateField(null=False)
    ava = models.CharField(max_length=200, blank=True, default='')

class Song(models.Model):
    name = models.CharField(max_length=100, null=False)
    owned = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    src = models.FileField(upload_to='media/')
    plays = models.IntegerField(null=True, default=0)
    likes = models.IntegerField(null=True, default=0)

class Playlist(models.Model):
    name = models.CharField(max_length=100, null=False)
    created = models.DateTimeField(auto_now_add=True)
    owned = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.BooleanField(default=False)

class Detailpl(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('playlist', 'song')

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followerusr')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followedusr')

    class Meta:
        unique_together = ('follower', 'followed')