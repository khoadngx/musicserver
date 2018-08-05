from django.db import models

class User(models.Model):
    usrname = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100, null=False)
    passwd = models.CharField(max_length=30, null=False)
    dob = models.DateField(null=False)
    ava = models.FileField(upload_to='media/', default='default_avatar.jpg')
    about = models.CharField(max_length=300, null=True)

class Song(models.Model):
    name = models.CharField(max_length=100, null=False)
    owned = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=30, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    ava = models.FileField(upload_to='media/', default='cover_default.png')
    src = models.FileField(upload_to='media/', null=True)
    plays = models.IntegerField(default=0, null=True)
    likes = models.IntegerField(default=0, null=True)

class Playlist(models.Model):
    name = models.CharField(max_length=100, null=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    owned = models.ForeignKey(User, on_delete=models.CASCADE)
    ava = models.FileField(upload_to='media/', default='default_playlist.png')
    likes = models.IntegerField(default=0, null=True)

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