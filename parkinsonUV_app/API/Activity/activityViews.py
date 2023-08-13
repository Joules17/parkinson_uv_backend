from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView
from .serializers import (
    ActivitySerializer, 
    ActivitySerializerWithoutPK
)

from rest_framework.views import APIView
from parkinsonUV_app.models import Activity, List, Patient, Therapist, Game_list
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

class GetActivitiesByTherapistDetailed(APIView): 
    def get(self, request, id_therapist):
        assigned_activities = Activity.objects.filter(id_therapist = id_therapist)
        result_patients = Patient.objects.filter(user_id__in = assigned_activities.values('id_patient'))
        result_list = List.objects.filter(id__in = assigned_activities.values('id_list'))

        result = []
        for activity in assigned_activities: 
            activity_data = {
                'id': activity.id,
                'activity_name': activity.name, 
                'description' : activity.description,
                'interval': activity.interval,
                'last_scheduled_date': activity.last_scheduled_date, 
                'id_list' : activity.id_list_id, 
                'id_patient' : activity.id_patient_id,
                'id_therapist' : activity.id_therapist_id 
            }
            print('Inspeccionemos', activity_data['id_list'])
            ## Buscar el objeto correspondiente en result_patients 
            patient = result_patients.filter(user_id = activity_data['id_patient'])
            patient = list(patient.values())[0]
            if patient: 
                ## Convertimos la informacion del paciente a diccionario 
                patient_data = {
                    'id_patient' : patient['user_id_id'], 
                    'id_type': patient['id_type'],
                    'patient_name': patient['name'],
                    'patient_lastname': patient['lastname'],
                    'patient_email': patient['email'],
                    'patient_cell': patient['cell'],
                    'patient_age': patient['age'],
                    'patient_gender': patient['gender'] 
                }
                
                ## agregamos campos al diccionario principal: 
                activity_data.update(patient_data)
            
            ## Buscar el objeto correspondiente en listas
            lista = result_list.filter(id = activity_data['id_list'])
            lista = list(lista.values())[0]

            if lista: 
                print(lista, 'VEAMOS QUE ES ESTO')
                ## Convertir Lista a un diccionario 
                lista_data = {
                    'id_list': lista['id'],
                    'lista_name': lista['name']
                }
                activity_data.update(lista_data)
            
            result.append(activity_data)
        return Response(result) 
            

    

        