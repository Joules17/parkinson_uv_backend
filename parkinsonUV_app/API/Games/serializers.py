from rest_framework import serializers
from parkinsonUV_app.models import Game, Game_type 

class GameTypeSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Game_type
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer): 
    id_type = serializers.SerializerMethodField()
    class Meta: 
        model = Game
        fields = '__all__' 

    def get_id_type(self, game):
        return game.id_type.type