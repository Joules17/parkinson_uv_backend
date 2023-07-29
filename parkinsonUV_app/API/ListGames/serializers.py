from rest_framework import serializers
from parkinsonUV_app.models import Game_list, List

class ListGamesSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Game_list
        fields = '__all__'  

class ListSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = List
        fields = '__all__'  
