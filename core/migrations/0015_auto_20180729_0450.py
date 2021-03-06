# Generated by Django 2.0.7 on 2018-07-29 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20180729_0450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followedusr', to='core.User')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followerusr', to='core.User')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('follower', 'followed')},
        ),
    ]
