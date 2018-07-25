# Generated by Django 2.0.7 on 2018-07-25 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180725_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='album',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='plays',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
