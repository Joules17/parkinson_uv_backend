from rest_framework.generics import UpdateAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from .serializers import (
    ListGamesSerializer, 
    ListSerializer
)

from parkinsonUV_app.models import List, Game_list
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView

import http.client
import json, os
from dotenv import load_dotenv

# List -------------------------------------------------------------------------------------------------------------
class ListCreateApi(CreateAPIView): 
    serializer_class = ListSerializer
    model = List
    permission_classes = [permissions.AllowAny]

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

## Game Types -------------------------------------------------------------------------------------------------

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