# Generated by Django 4.2.2 on 2023-08-01 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parkinsonUV_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='password',
        ),
    ]