# Generated by Django 2.0.7 on 2018-07-25 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_song_src'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='src',
            field=models.FileField(upload_to=''),
        ),
    ]
