from rest_framework.generics import UpdateAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from .serializers import (
    ParkinsonSerializer
)

from parkinsonUV_app.models import Parkinson_phase
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView

import http.client
import json, os
from dotenv import load_dotenv

class ParkinsonCreateApi(CreateAPIView): 
    serializer_class = ParkinsonSerializer
    model = Parkinson_phase
    permission_classes = [permissions.AllowAny]

class ParkinsonUpdateApi(UpdateAPIView): 
    serializer_class = ParkinsonSerializer
    model = Parkinson_phase
    permission_classes = [permissions.AllowAny]
    queryset = Parkinson_phase.objects.all()

class ParkinsonRetrieveApi(RetrieveAPIView): 
    serializer_class = ParkinsonSerializer
    model = Parkinson_phase
    permission_classes = [permissions.AllowAny]
    queryset = Parkinson_phase.objects.all()

class RetreiveAllParkinsons(ListAPIView): 
    serializer_class = ParkinsonSerializer
    model = Parkinson_phase
    permission_classes = [permissions.AllowAny]
    queryset = Parkinson_phase.objects.all()

class DeleteParkinsonApi(DestroyAPIView): 
    serializer_class = ParkinsonSerializer
    model = Parkinson_phase 
    permission_classes = [permissions.AllowAny]
    queryset = Parkinson_phase.objects.all()

    def delete(self, request, pk, format= None): 
        parkinson_phase = self.get_object()
        parkinson_phase.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
