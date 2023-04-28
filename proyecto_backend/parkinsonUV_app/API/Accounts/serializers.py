from rest_framework import serializers
from parkinsonUV_app.models import Account, Patient, Therapist

class AccountSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Account, 
        fields = ['id', 'id_type', 'password', 'email', 'user_status']

class AccountAuthSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Account, 
        fields = ['id']

class ActivationAccountSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Account,   
        fields = ['id', 'user_status']

## NESTED SERIALIZERS

class RetreiveTherapistAccountSerializer(serializers.ModelSerializer): 
    id = AccountSerializer()

    class Meta: 
        model = Therapist
        fields = ['id', 'id_type', 'name', 'lastname', 'email', 'cell']

class RetreivePatientAccountSerializer(serializers.ModelSerializer): 
    id = AccountSerializer()
    
    class Meta: 
        model = Patient
        fields = ['id', 'id_type', 'name', 'lastname', 'email', 'cell', 'age', 'gender', 'id_parkinson_phase', 'id_therapist']

