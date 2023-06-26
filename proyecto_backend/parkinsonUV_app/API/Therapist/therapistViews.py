from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from .serializers import (
    TherapistSerializer, 
    TherapistSerializerWithoutPk
)
from rest_framework.views import APIView
from parkinsonUV_app.models import Account, Therapist
from rest_framework.response import Response
from rest_framework import permissions, status

class TherapistCreateApi(CreateAPIView):
    serializer_class = TherapistSerializer
    model = Therapist
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        account = Account.objects.get(user_id = request.data['user_id'])
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            serializer.save(user_id = account)
            return Response({'message': 'El terapeuta se creo correctamente', 'data': serializer.data }, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class TherapistUpdateApi(UpdateAPIView):
    serializer_class = TherapistSerializerWithoutPk
    permission_classes = [permissions.AllowAny]
    queryset = Therapist.objects.all()

class TherapistRetrieveApi(RetrieveAPIView):
    serializer_class = TherapistSerializer
    model = Therapist
    permission_classes = [permissions.AllowAny]
    queryset = Therapist.objects.all()

class getTherapistDetailed(APIView): 
    def get(self, request, user_id): 
        therapist = Therapist.objects.filter(user_id = user_id)
        account = Account.objects.filter(user_id = user_id)
        
        therapist_data = {
            'user_id' : account[0].user_id, 
            'document_id' : account[0].document_id, 
            'document_type' : account[0].document_type, 
            'user_picture' : account[0].user_picture, 
            'email': account[0].email,
            'user_status' : account[0].user_status, 
            'name' : therapist[0].name, 
            'lastname' : therapist[0].lastname, 
            'cell': therapist[0].cell
        }

        return Response(therapist_data)

class RetreiveAllTherapists(ListAPIView):
    serializer_class = TherapistSerializer
    model = Therapist
    permission_classes = [permissions.AllowAny]
    queryset = Therapist.objects.all()