from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView
from .serializers import (
    ActivitySerializer, 
    ActivitySerializerWithoutPK
)

from rest_framework.views import APIView
from parkinsonUV_app.models import Activity, List, Patient, Therapist
from rest_framework.response import Response
from rest_framework import permissions, status

class ActivityCreateAPI(CreateAPIView): 
    serializer_class = ActivitySerializer
    model = Activity
    permission_classes = [permissions.AllowAny]

    def post(self, request): 
        print(request.data)
        list_obj = List.objects.get(id = request.data['id_list'])
        patient = Patient.objects.get(user_id = request.data['id_patient'])
        therapist = Therapist.objects.get(user_id = request.data['id_therapist'])
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid(): 
            serializer.save(id_list = list_obj)
            serializer.save(id_patient = patient)
            serializer.save(id_therapist = therapist)
            return Response({'message' : '¡La Actividad fue creada con exito!'})
        else: 
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ActivityUpdateAPI(UpdateAPIView): 
    serializer_class = ActivitySerializerWithoutPK
    permission_classes = [permissions.AllowAny]
    queryset = Activity.objects.all()

class ActivityRetreiveAPI(RetrieveAPIView): 
    serializer_class = ActivitySerializer
    model = Activity
    permission_classes = [permissions.AllowAny]
    queryset = Activity.objects.all()

class RetreiveAllActivities(ListAPIView): 
    serializer_class = ActivitySerializer
    model = Activity
    permission_classes = [permissions.AllowAny]
    queryset = Activity.objects.all()

class DeleteActivityApi(DestroyAPIView): 
    serializer_class = ActivitySerializer
    model = Activity
    permission_classes = [permissions.AllowAny]
    queryset = Activity.objects.all()

    def delete(self, request, pk, format = None): 
        Activity = self.get_object()
        Activity.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)