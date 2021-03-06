# Generated by Django 2.0.7 on 2018-08-05 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_playlist_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='ava',
            field=models.FileField(default='media/default_playlist.png', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='ava',
            field=models.FileField(default='media/cover_default.png', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='ava',
            field=models.FileField(default='media/default_avatar.png', upload_to='media/'),
        ),
    ]
