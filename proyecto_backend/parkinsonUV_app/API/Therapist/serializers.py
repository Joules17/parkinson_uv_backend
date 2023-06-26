from rest_framework import serializers
from parkinsonUV_app.models import Therapist

## Terapeutas 

class TherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        fields = '__all__'  

class TherapistSerializerWithoutPk(serializers.ModelSerializer): 
    class Meta: 
        model = Therapist
        fields = ['id_type', 'name', 'lastname', 'email', 'cell']