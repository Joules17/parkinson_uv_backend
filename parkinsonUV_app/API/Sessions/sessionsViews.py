from rest_framework.generics import UpdateAPIView, CreateAPIView,  ListAPIView, RetrieveAPIView, DestroyAPIView
from .serializer import ( 
    SessionSerializer, 
    SessionSerializerWithoutPK
)

from parkinsonUV_app.models import Session, Activity, Patient, Therapist
from rest_framework.response import response
from rest_framework import permissions, status

class SessionCreateAPI(CreateAPIView):
    serializer_class = SessionSerializer
    model = Session
    permission_classes = [permissions.AllowAny]

    def post(self, request): 
        activity = Activity.objects.get(id = request.data['id_activity'])
        patient = Patient.objects.get(user_id = request.data['id_patient'])
        therapist = Therapist.objects.get(user_id = request.data['id_therapist'])
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save(id_activity = activity)
            serializer.save(id_patient = patient)
            serializer.save(id_therapist = therapist)
            return Response({'message' : '¡La Sesión fue creada con exito!'})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class SessionUpdateAPI(UpdateAPIView):
    serializer_class = SessionSerializerWithoutPK
    permission_classes = [permissions.AllowAny]
    queryset = Session.objects.all()

class SessionRetreiveAPI(RetrieveAPIView):
    serializer_class = SessionSerializer
    model = Session
    permission_classes = [permissions.AllowAny]
    queryset = Session.objects.all()

class RetreiveAllSessions(ListAPIView):
    serializer_class = SessionSerializer
    model = Session
    permission_classes = [permissions.AllowAny]
    queryset = Session.objects.all()

class DeleteSessionApi(DestroyAPIView):
    serializer_class = SessionSerializer
    model = Session
    permission_classes = [permissions.AllowAny]
    queryset = Session.objects.all()

    def delete(self, request, pk, format = None):
        Session = self.get_object()
        Session.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        


