from rest_framework.generics import UpdateAPIView, CreateAPIView,  ListAPIView, RetrieveAPIView, DestroyAPIView
from .serializers import ( 
    SessionSerializer, 
    SessionSerializerWithoutPK
)

from parkinsonUV_app.models import Session, Activity, Patient, Therapist
from rest_framework.response import Response
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

class DeleteSessionAPI(DestroyAPIView):
    serializer_class = SessionSerializer
    model = Session
    permission_classes = [permissions.AllowAny]
    queryset = Session.objects.all()

    def delete(self, request, pk, format = None):
        Session = self.get_object()
        Session.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
class SessionIdView(RetrieveAPIView):
    def get(self, request, id_activity, id_patient):
        try:
            session = Session.objects.get(id_activity=id_activity, id_patient=id_patient)
            session_id = session.id
            return Response({'session_id': session_id}, status=status.HTTP_200_OK)
        except Session.DoesNotExist:
            return Response({'error': 'Sesión no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
