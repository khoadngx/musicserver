# Generated by Django 2.0.7 on 2018-07-25 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180725_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
