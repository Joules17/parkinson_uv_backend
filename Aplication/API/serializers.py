from rest_framework import serializers
from Aplication.models import Patient

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'id_type', 'name', 'lastname', 'email', 'cell', 'age', 'gender', 'is_active', 'id_parkinson_phase', 'id_therapist']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'id_type', 'name', 'lastname', 'email', 'cell', 'age', 'gender', 'is_active', 'id_parkinson_phase', 'id_therapist']
