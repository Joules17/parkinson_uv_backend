from rest_framework import serializers
from ..models import Therapist, Patient

## Terapeutas 

class TherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        fields = '__all__'
    
## Pacientes

class PatientSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Patient
        fields = '__all__'

## Games 

