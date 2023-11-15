from rest_framework import serializers
from parkinsonUV_app.models import Game_list, List, Game
from ..Games.serializers import GameSerializer

class ListGamesSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Game_list
        fields = '__all__'  

class ListGamesSerializerSetting(serializers.ModelSerializer):
    class Meta: 
        model = Game_list
        fields = ['setting'] 

class ListSerializer(serializers.ModelSerializer): 
    games = serializers.SerializerMethodField()
    class Meta: 
        model = List
        fields = '__all__'

    def get_games(self, list_obj):
        games_data = Game_list.objects.filter(id_list=list_obj)
        games_with_setting = []

        for game_data in games_data:
            game_serializer = GameSerializer(game_data.id_game)
            game_with_setting = game_serializer.data
            game_with_setting["setting"] = game_data.setting
            game_with_setting["id_game_list"] = game_data.id  
            game_with_setting["is_played"] = game_data.is_played
            games_with_setting.append(game_with_setting)

        return games_with_setting
    
class ListCreateSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = List
        fields = '__all__'
