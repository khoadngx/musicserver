# Generated by Django 2.0.7 on 2018-07-25 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20180725_0243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detailpl',
            old_name='playlistid',
            new_name='playlist',
        ),
        migrations.RenameField(
            model_name='detailpl',
            old_name='songid',
            new_name='song',
        ),
        migrations.AlterUniqueTogether(
            name='detailpl',
            unique_together={('playlist', 'song')},
        ),
    ]