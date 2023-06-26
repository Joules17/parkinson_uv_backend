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