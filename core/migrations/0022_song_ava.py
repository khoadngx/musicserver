# Generated by Django 2.0.7 on 2018-07-31 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20180731_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='ava',
            field=models.FileField(null=True, upload_to='media/'),
        ),
    ]
