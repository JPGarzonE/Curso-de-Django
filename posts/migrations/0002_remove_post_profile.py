# Generated by Django 3.0.2 on 2020-03-20 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='profile',
        ),
    ]
