# Generated by Django 4.2.2 on 2023-11-16 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkinsonUV_app', '0010_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='total_rounds_played',
            field=models.IntegerField(default=0),
        ),
    ]
