# Generated by Django 4.2.2 on 2023-10-22 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkinsonUV_app', '0008_logs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='date_start',
            field=models.DateTimeField(null=True),
        ),
    ]
