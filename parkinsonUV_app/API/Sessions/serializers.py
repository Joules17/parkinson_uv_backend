from rest_framework import serializers
from parkinsonUV_app.models import Session

class SessionSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Session 
        fields = ['id', 'date_start', 'date_end', 'log', 'id_activity', 'id_patient', 'id_therapist']

class SessionSerializerWithoutPK(serializers.ModelSerializer): 
    class Meta: 
        model = Session 
        fields = ['date_start', 'date_end', 'log', 'id_activity', 'id_patient', 'id_therapist']
