from rest_framework.generics import UpdateAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from .serializers import (
    ListGamesSerializer, 
    ListSerializer,
    ListGamesSerializerSetting,
    ListCreateSerializer
)

from parkinsonUV_app.models import List, Game_list, Game
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView

import http.client
import json, os
from dotenv import load_dotenv

# List -------------------------------------------------------------------------------------------------------------
from rest_framework.response import Response
from django.db import transaction

class ListCreateApi(CreateAPIView): 
    serializer_class = ListCreateSerializer
    model = List
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        games_data = self.request.data.get('games', [])

        with transaction.atomic():
            game_list = serializer.save()

            for game_id in games_data:
                game = Game.objects.get(id=game_id)

                # Aquí define el valor adecuado para el campo "setting" de cada juego
                setting_data = {
                    "field1": "value1",
                    "field2": "value2",
                    # Agrega aquí los campos y valores que necesites para "setting"
                }

                # Crea el objeto Game_list con el valor "setting" proporcionado
                Game_list.objects.create(id_list=game_list, id_game=game, setting=setting_data)

class ListUpdateApi(UpdateAPIView): 
    serializer_class = ListSerializer
    model = List
    permission_classes = [permissions.AllowAny]
    queryset = List.objects.all()

class ListRetreiveApi(RetrieveAPIView): 
    serializer_class = ListSerializer
    model = List
    permission_classes = [permissions.AllowAny]
    queryset = List.objects.all()

class RetreiveAllList(ListAPIView): 
    serializer_class = ListSerializer
    model = List
    permission_classes = [permissions.AllowAny]
    queryset = List.objects.all()

class DeleteListApi(DestroyAPIView): 
    serializer_class = ListSerializer
    model = List 
    permission_classes = [permissions.AllowAny]
    queryset = List.objects.all()

    def delete(self, request, pk, format= None): 
        List = self.get_object()
        List.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

## Game List -------------------------------------------------------------------------------------------------

class GameListCreateApi(CreateAPIView): 
    serializer_class = ListGamesSerializer
    model = Game_list
    permission_classes = [permissions.AllowAny]
    queryset = Game_list.objects.all()

class GameListUpdateApi(UpdateAPIView): 
    serializer_class = ListGamesSerializer
    model = Game_list
    permission_classes = [permissions.AllowAny]
    queryset = Game_list.objects.all()

class GameListSettingUpdateApi(UpdateAPIView): 
    serializer_class = ListGamesSerializerSetting
    permission_classes = [permissions.AllowAny]
    queryset = Game_list.objects.all()

class GameListRetreiveApi(RetrieveAPIView): 
    serializer_class = ListGamesSerializer
    model = Game_list
    permission_classes = [permissions.AllowAny]
    queryset = Game_list.objects.all()

class RetreiveAllGameList(ListAPIView): 
    serializer_class = ListGamesSerializer
    model = Game_list
    permission_classes = [permissions.AllowAny]
    queryset = Game_list.objects.all()

class DeleteGameListApi(DestroyAPIView): 
    serializer_class = ListGamesSerializer
    model = Game_list 
    permission_classes = [permissions.AllowAny]
    queryset = Game_list.objects.all()

    def delete(self, request, pk, format= None): 
        Game_list = self.get_object()
        Game_list.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)