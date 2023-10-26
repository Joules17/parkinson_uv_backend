from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView
from .serializers import (
    ActivitySerializer,
    ActivitySerializerWithoutPK,
    ActivitySerializerWithoutPKStatus
)

from rest_framework.views import APIView
from parkinsonUV_app.models import Activity, List, Patient, Therapist
from rest_framework.response import Response
from rest_framework import permissions, status

from datetime import date
from django.http import HttpResponse

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

class GetActivitiesByTherapistDetailed(APIView):
    def get(self, request, id_therapist):
        assigned_activities = Activity.objects.filter(id_therapist = id_therapist)

        result = []
        for activity in assigned_activities:
            activity_data = {
                'id': activity.id,
                'activity_name': activity.name,
                'description' : activity.description,
                'start_date': activity.start_date,
                'end_date': activity.end_date,
                'status': activity.status,
                'id_patient' : activity.id_patient_id,
                'id_type': activity.id_patient.id_type,
                'patient_name': activity.id_patient.name,
                'patient_lastname': activity.id_patient.lastname,
                'patient_picture': activity.id_patient.user_id.user_picture,
                'id_therapist' : activity.id_therapist_id,
                'therapist_name' : activity.id_therapist.name,
                'therapist_lastname' : activity.id_therapist.lastname,
                'therapist_picture': activity.id_therapist.user_id.user_picture,
                'id_list' : activity.id_list_id,
                'lista_name': activity.id_list.name
            }
            result.append(activity_data)
        return Response(result)

class GetActivitiesByPatientDetailed(APIView):
    def get(self, request, id_patient):
        assigned_activities = Activity.objects.filter(id_patient = id_patient)
        result = []
        for activity in assigned_activities:
            activity_data = {
            'id': activity.id,
            'activity_name': activity.name,
            'description' : activity.description,
            'start_date': activity.start_date,
            'end_date': activity.end_date,
            'status': activity.status,
            'id_patient' : activity.id_patient_id,
            'id_type': activity.id_patient.id_type,
            'patient_name': activity.id_patient.name,
            'patient_lastname': activity.id_patient.lastname,
            'patient_picture': activity.id_patient.user_id.user_picture,
            'id_therapist' : activity.id_therapist_id,
            'therapist_name' : activity.id_therapist.name,
            'therapist_lastname' : activity.id_therapist.lastname,
            'therapist_picture': activity.id_therapist.user_id.user_picture,
            'id_list' : activity.id_list_id,
            'lista_name': activity.id_list.name
            }
            result.append(activity_data)
        return Response(result)


class UpdateActivitiesStatus(APIView):
     def get(self, request):
        # update activities statuses according to date
        activities_to_update = Activity.objects.filter(status='Pendiente', end_date__lt=date.today())
        activities_to_update.update(status='Caducado')

        return HttpResponse('Estado de actividades actualizado correctamente')
     
class ActivityStatusUpdateAPI(UpdateAPIView):
    serializer_class = ActivitySerializerWithoutPKStatus
    permission_classes = [permissions.AllowAny]
    queryset = Activity.objects.all()

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        partial = request.data.get("status")  # Obtén el nuevo valor del campo 'status' desde la solicitud
        if partial is not None:
            instance.status = partial  # Actualiza el campo 'status'
            instance.save()
            return Response(self.get_serializer(instance).data)
        return Response({"status": "No se proporcionó el campo 'status' en la solicitud."}, status=status.HTTP_400_BAD_REQUEST)




