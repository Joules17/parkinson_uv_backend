from rest_framework.generics import UpdateAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from .serializers import (
    ListGamesSerializer, 
    ListSerializer,
    ListGamesSerializerSetting,
    ListCreateSerializer
)
from rest_framework.views import APIView
from parkinsonUV_app.models import List, Game_list, Game
from rest_framework.response import Response
from rest_framework import permissions, status

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

class RetreiveTherapistLists(APIView): 
    def get(self, request, id_therapist): 
        created_list = List.objects.filter(id_therapist = id_therapist)
        ## arreglo result con todas las listas asignadas al id_therapist del parametro 
        result = []
        for lista in created_list: 
            data_list = {
                "id": lista.id,
                "name": lista.name,
                "id_therapist" : lista.id_therapist_id
            }
            lista_games = Game_list.objects.filter(id_list = lista.id)
            result_lista_games = []
            for juego in lista_games: 
                game_info = {
                    "id" : juego.id_game.id, 
                    "id_type": juego.id_game.id_type.type,
                    "name" : juego.id_game.name,
                    "description" : juego.id_game.description,
                    "game_picture" : juego.id_game.game_picture,
                    "setting" : juego.setting, 
                    "id_game_list" : juego.id
                }
                result_lista_games.append(game_info)
            data_list["games"] = result_lista_games
            result.append(data_list)
            
        return Response(result)

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