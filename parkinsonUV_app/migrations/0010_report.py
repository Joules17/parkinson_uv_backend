# Generated by Django 4.2.2 on 2023-11-14 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parkinsonUV_app', '0009_alter_session_date_end_alter_session_date_start'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('total_played_time', models.IntegerField(default=0)),
                ('avg_round_time', models.IntegerField(default=0)),
                ('total_errors', models.IntegerField(default=0)),
                ('total_games_played', models.IntegerField(default=0)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkinsonUV_app.patient')),
            ],
        ),
    ]
