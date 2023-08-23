from rest_framework import serializers
from parkinsonUV_app.models import Activity

class ActivitySerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Activity
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'status', 'id_list', 'id_patient', 'id_therapist']

class ActivitySerializerWithoutPK(serializers.ModelSerializer): 
    class Meta: 
        model = Activity
        fields = ['name', 'description', 'start_date', 'end_date', 'status', 'id_list', 'id_patient', 'id_therapist']