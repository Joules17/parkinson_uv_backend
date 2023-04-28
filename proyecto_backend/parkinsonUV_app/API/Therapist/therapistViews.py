from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from .serializers import (
    TherapistSerializer, 
    TherapistSerializerWithoutPk
)
from parkinsonUV_app.models import Account, Therapist
from rest_framework.response import Response
from rest_framework import permissions, status

class TherapistCreateApi(CreateAPIView):
    serializer_class = TherapistSerializer
    model = Therapist
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        account = Account.objects.get(user_id = request.data['id'])
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

class RetreiveAllTherapists(ListAPIView):
    serializer_class = TherapistSerializer
    model = Therapist
    permission_classes = [permissions.AllowAny]
    queryset = Therapist.objects.all()