from rest_framework.generics import UpdateAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from .serializers import (
    GameSerializer, 
    GameTypeSerializer
)

from parkinsonUV_app.models import Game, Game_type
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView

import http.client
import json, os
from dotenv import load_dotenv

# Game -------------------------------------------------------------------------------------------------------------
class GameCreateApi(CreateAPIView): 
    serializer_class = GameSerializer
    model = Game
    permission_classes = [permissions.AllowAny]

class GameUpdateApi(UpdateAPIView): 
    serializer_class = GameSerializer
    model = Game
    permission_classes = [permissions.AllowAny]
    queryset = Game.objects.all()

class GameRetreiveApi(RetrieveAPIView): 
    serializer_class = GameSerializer
    model = Game
    permission_classes = [permissions.AllowAny]
    queryset = Game.objects.all()

class RetreiveAllGames(ListAPIView): 
    serializer_class = GameSerializer
    model = Game
    permission_classes = [permissions.AllowAny]
    queryset = Game.objects.all()

class RetreiveAllGamesWithType(APIView): 
    def get(self, request): 
        games = Game.objects.all()

        result_types= Game_type.objects.filter(id__in = games.values('id_type'))
        result = []
        for game in games:
            game_data = {
                'id': game.id,
                'name': game.name,
                'description': game.description,
                'game_picture': game.game_picture,
                'id_type_id': game.id_type_id,
            }
            game_type = result_types.filter(id = game_data['id_type_id'])
            game_type = list(game_type.values())[0]
            
            
            if game_type: 
                game_type_data = {
                    'type': game_type['type']
                }
                game_data.update(game_type_data)
            
            result.append(game_data)

        return Response(result)

class DeleteGameApi(DestroyAPIView): 
    serializer_class = GameSerializer
    model = Game 
    permission_classes = [permissions.AllowAny]
    queryset = Game.objects.all()

    def delete(self, request, pk, format= None): 
        game = self.get_object()
        game.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

## Game Types -------------------------------------------------------------------------------------------------

class GameTypeCreateApi(CreateAPIView): 
    serializer_class = GameTypeSerializer
    model = Game_type
    permission_classes = [permissions.AllowAny]
    queryset = Game_type.objects.all()

class GameTypeUpdateApi(UpdateAPIView): 
    serializer_class = GameTypeSerializer
    model = Game_type
    permission_classes = [permissions.AllowAny]
    queryset = Game_type.objects.all()

class GameTypeRetreiveApi(RetrieveAPIView): 
    serializer_class = GameTypeSerializer
    model = Game_type
    permission_classes = [permissions.AllowAny]
    queryset = Game_type.objects.all()

class RetreiveAllGameTypes(ListAPIView): 
    serializer_class = GameTypeSerializer
    model = Game_type
    permission_classes = [permissions.AllowAny]
    queryset = Game_type.objects.all()

class DeleteGameTypeApi(DestroyAPIView): 
    serializer_class = GameTypeSerializer
    model = Game_type 
    permission_classes = [permissions.AllowAny]
    queryset = Game_type.objects.all()

    def delete(self, request, pk, format= None): 
        game_type = self.get_object()
        game_type.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)