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
    description = models.CharField(max_length= 500, default = 'N/A')
    id_type = models.ForeignKey(Game_type, on_delete=models.CASCADE)
    game_picture = models.CharField(max_length=500, default = 'N/A')

class Account(models.Model): 
    user_id = models.CharField(primary_key = True, max_length = 200)
    id_type = models.IntegerField()
    document_id = models.IntegerField(max_length= 50, default = 0000000000)
    document_type = models.CharField(max_length= 40, default = 'C.C.')
    user_picture = models.CharField(max_length=400, default = 'NN')
    password = models.CharField(max_length=200)
    email = models.EmailField()
    user_status = models.BooleanField(default = True)

class Therapist(models.Model):
    user_id = models.ForeignKey(Account, on_delete = models.CASCADE, related_name= 'Therapist', primary_key= True)
    id_type = models.IntegerField()
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    cell = models.CharField(max_length=10)

class Patient(models.Model):
    user_id = models.ForeignKey(Account, on_delete = models.CASCADE, related_name= 'Patient', primary_key= True)
    id_type = models.IntegerField()
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    cell = models.CharField(max_length=10)
    age = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    id_parkinson_phase = models.ForeignKey(Parkinson_phase, on_delete=models.CASCADE)
    id_therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)

class Game_list(models.Model):
    id_list = models.ForeignKey('List', on_delete=models.CASCADE)
    id_game = models.ForeignKey(Game, on_delete=models.CASCADE)
    setting = models.JSONField()

class List(models.Model):
    name = models.CharField(max_length=100)
    id_therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    id_patient = models.ManyToManyField(Patient, null="true")
    games = models.ManyToManyField(Game, through=Game_list)

class Registers(models.Model):
    id_list = models.ForeignKey(List, on_delete=models.CASCADE)
    id_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    id_game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date = models.DateField()
    log = models.JSONField()