from rest_framework.generics import UpdateAPIView, CreateAPIView,  ListAPIView, RetrieveAPIView, DestroyAPIView
from .serializers import ( 
    SessionSerializer, 
    SessionSerializerWithoutPK
)

from rest_framework.views import APIView
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
        
class GetSessionsByTherapistDetailed(APIView): 
    def get(self, request, id_therapist): 
        assigned_sessions = Session.objects.filter(id_therapist = id_therapist)

        result = []
        for session in assigned_sessions: 
            session_data = {
                "id": session.id,
                "date_start" : session.date_start,
                "date_end" : session.date_end,
                "id_activity" : session.id_activity.id,
                "activity_name" : session.id_activity.name,
                "activity_status" : session.id_activity.status,
                "id_patient" : session.id_patient_id,
                "patient_name" : session.id_patient.name,
                "patient_lastname" : session.id_patient.lastname,
                "patient_picture" : session.id_patient.user_id.user_picture,
                "id_therapist" : session.id_therapist_id,
                "therapist_name" : session.id_therapist.name,
                "therapist_lastname" : session.id_therapist.lastname,
                "therapist_picture" : session.id_therapist.user_id.user_picture
            }

            result.append(session_data)
        return Response(result)
