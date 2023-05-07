from rest_framework import serializers
from parkinsonUV_app.models import Game, Game_type

class GameSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Game
        fields = '__all__'  

class GameTypeSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Game_type
        fields = '__all__'