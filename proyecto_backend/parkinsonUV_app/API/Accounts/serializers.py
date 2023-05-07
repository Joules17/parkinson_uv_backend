from rest_framework import serializers
from parkinsonUV_app.models import Account, Patient, Therapist

class AccountSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Account
        fields = '__all__'  

class AccountAuthSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Account
        fields = ['user_id']

class ActivationAccountSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Account   
        fields = ['user_id', 'user_status']

## NESTED SERIALIZERS

class RetreiveTherapistAccountSerializer(serializers.ModelSerializer): 
    user_id = AccountSerializer()

    class Meta: 
        model = Therapist
        fields = ['user_id', 'id_type', 'name', 'lastname', 'email', 'cell']

class RetreivePatientAccountSerializer(serializers.ModelSerializer): 
    id = AccountSerializer()
    
    class Meta: 
        model = Patient
        fields = ['user_id', 'id_type', 'name', 'lastname', 'email', 'cell', 'age', 'gender', 'id_parkinson_phase', 'id_therapist']

