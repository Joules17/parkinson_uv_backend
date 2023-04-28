from rest_framework import serializers
from parkinsonUV_app.models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'id_type', 'name', 'lastname', 'email', 'cell', 'age', 'gender', 'id_parkinson_phase', 'id_therapist']

class PatientSerializerWithoutPk(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id_type', 'name', 'lastname', 'email', 'cell', 'age', 'gender', 'id_parkinson_phase', 'id_therapist']