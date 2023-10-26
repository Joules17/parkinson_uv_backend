from rest_framework import serializers
from parkinsonUV_app.models import Logs

class LogsSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Logs 
        fields = ['id', 'id_session', 'id_game_list', 'log']

class LogsSerializerWithoutPK(serializers.ModelSerializer): 
    class Meta: 
        model = Logs 
        fields = ['id_session', 'id_game_list', 'log']

class LogSerializerWithGameData(serializers.ModelSerializer):
    name = serializers.CharField(source='id_game_list.id_game.name', read_only=True)
    game_picture = serializers.CharField(source='id_game_list.id_game.game_picture', read_only=True)

    class Meta:
        model = Logs
        fields = '__all__'
