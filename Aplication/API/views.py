from rest_framework import generics
from Aplication.API.serializers import (
    AccountSerializer, 
    UserSerializer
)

from Aplication.models import Patient
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from django.shortcuts import get_object_or_404


#Views para CREATE


class UserCreateApi(generics.CreateAPIView):
    serializer_class = UserSerializer
    model = Patient
    template_name = None
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        patient = Patient.objects.get(id = request.data['id'])
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            serializer.save(id = patient)
            return Response({'message': 'Se creo correctamente el paciente', 'data': serializer.data }, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
