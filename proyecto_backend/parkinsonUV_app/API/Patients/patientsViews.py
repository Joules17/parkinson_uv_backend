from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView
from .serializers import (
    PatientSerializer, 
    PatientSerializerWithoutPk
)
from parkinsonUV_app.models import Account, Patient
from rest_framework.response import Response
from rest_framework import permissions, status

class PatientCreateApi(CreateAPIView):
    serializer_class = PatientSerializer
    model = Patient
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        print(request.data)
        account = Account.objects.get(user_id = request.data['user_id'])
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            serializer.save(user_id = account)
            return Response({'message': 'La cuenta de paciente fue creada con exito', 'data': serializer.data }, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class PatientUpdateApi(UpdateAPIView):
    serializer_class = PatientSerializerWithoutPk
    permission_classes = [permissions.AllowAny]
    queryset = Patient.objects.all()

class PatientRetrieveApi(RetrieveAPIView):
    serializer_class = PatientSerializer
    model = Patient
    permission_classes = [permissions.AllowAny]
    queryset = Patient.objects.all()

class RetreiveAllPatients(ListAPIView):
    serializer_class = PatientSerializer
    model = Patient
    permission_classes = [permissions.AllowAny]
    queryset = Patient.objects.all()