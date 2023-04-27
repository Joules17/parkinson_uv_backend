from django.db import models
# Create your models here.

class Parkinson_phase(models.Model):
    id = models.AutoField(primary_key=True)
    phase = models.CharField(max_length=100)

class Game_type(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)

class Game_settings(models.Model):
    id = models.AutoField(primary_key=True)
    level = models.IntegerField()
    time_seconds = models.IntegerField()
    specifications = models.JSONField()

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    id_type = models.ForeignKey(Game_type, on_delete=models.CASCADE)

class Therapist(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    id_type = models.CharField(max_length=4)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    cell = models.CharField(max_length=10)

class Patient(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    id_type = models.CharField(max_length=4)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    cell = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=3)
    is_active = models.BooleanField()
    id_parkinson_phase = models.ForeignKey(Parkinson_phase, on_delete=models.CASCADE)
    id_therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)

class List(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    id_therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    id_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

class Game_list(models.Model):
    id_list = models.ForeignKey(List, on_delete=models.CASCADE)
    id_game = models.ForeignKey(Game, on_delete=models.CASCADE)
    id_setting = models.ForeignKey(Game_settings, on_delete=models.CASCADE)

class Registers(models.model):
    id_list = models.ForeignKey(List, on_delete=models.CASCADE)
    id_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    id_game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date = models.DateField()
    log = models.JSONField()