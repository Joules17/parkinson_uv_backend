from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, ListAPIView
from .serializers import (
    PatientSerializer, 
    PatientSerializerWithoutPk, 
    PatientSerializerAssignee
)
from rest_framework.views import APIView
from parkinsonUV_app.models import Account, Patient, Parkinson_phase, Therapist
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

class GetPatientDetailed(APIView): 
    def get(self, request, user_id): 
        patient = Patient.objects.filter(user_id = user_id)
        account = Account.objects.filter(user_id = user_id)
        therapist = Therapist.objects.filter(user_id = patient[0].id_therapist_id)
        parkinson = Parkinson_phase.objects.filter(id = patient[0].id_parkinson_phase_id)

        patient_data = {
            'id_type': patient[0].id_type, 
            'name': patient[0].name,
            'lastname': patient[0].lastname, 
            'email': patient[0].email, 
            'cell': patient[0].cell, 
            'age': patient[0].age, 
            'gender': patient[0].gender, 
            'id_parkinson_phase_id': patient[0].id_parkinson_phase_id, 
            'id_therapist_id': patient[0].id_therapist_id, 
            'user_id': account[0].user_id, 
            'user_status': account[0].user_status, 
            'document_id': account[0].document_id, 
            'document_type': account[0].document_type, 
            'user_picture': account[0].user_picture, 
            'parkinson_phase': parkinson[0].phase, 
            'therapist_name': therapist[0].name, 
            'therapist_lastname': therapist[0].lastname 
        } 
        return Response(patient_data)

class RetreiveTherapistPatients(APIView):
    def get(self, request, id_therapist):
        assigned_patients = Patient.objects.filter(id_therapist=id_therapist)
        unassigned_patients = Patient.objects.filter(id_therapist="111")

        # Union de ambas consultas
        merge_patients = assigned_patients | unassigned_patients

        # Obtener los datos de la cuenta para los pacientes asignados
        result_accounts = Account.objects.filter(user_id__in=merge_patients.values('user_id'))

        ## Obtener los datos de parkinson phase para los pacientes asignados
        result_phases = Parkinson_phase.objects.filter(id__in = merge_patients.values('id_parkinson_phase_id'))

        # Juntar los datos de merge_patients y result_accounts
        result = []
        for patient in merge_patients:
            patient_data = {
                'id_type': patient.id_type,
                'name': patient.name,
                'lastname': patient.lastname,
                'email': patient.email,
                'cell': patient.cell,
                'age': patient.age,
                'gender': patient.gender,
                'id_parkinson_phase_id': patient.id_parkinson_phase_id,
                'id_therapist_id': patient.id_therapist_id,
                'user_id': patient.user_id_id,
            }

            # Buscar el objeto correspondiente en result_accounts
            account = result_accounts.filter(user_id=patient_data['user_id'])
            account = list(account.values())[0]
            if account:
                # Convertir el objeto Account en un diccionario
                account_data = {
                    'document_id': account['document_id'],
                    'document_type': account['document_type'],
                    'user_picture': account['user_picture'],
                    'user_status': account['user_status']
                }

                # Agregar los campos de la cuenta al diccionario de datos del paciente
                patient_data.update(account_data)

            # Buscar el objeto correspondiente en result_phases
            print('veamos aqui un momento', patient_data['id_parkinson_phase_id'])
            phases = result_phases.filter(id = patient_data['id_parkinson_phase_id'])
            phases = list(phases.values())[0]
            if phases:
                # Convertir phases a un diccionario 
                phases_data = {
                    'parkinson_phase' : phases['phase']
                }

                patient_data.update(phases_data)

            result.append(patient_data)

        print(result, 'cual es el problema???')
        return Response(result)
    
class PatientUpdateAssigneeApi(UpdateAPIView): 
    serializer_class = PatientSerializerAssignee
    permission_classes = [permissions.AllowAny]
    queryset = Patient.objects.all()