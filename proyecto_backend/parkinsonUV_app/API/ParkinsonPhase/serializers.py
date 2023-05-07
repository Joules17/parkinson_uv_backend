from rest_framework import serializers
from parkinsonUV_app.models import Parkinson_phase

class ParkinsonSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Parkinson_phase
        fields = '__all__'  
