from .serializers import ReportSerializer
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView
from parkinsonUV_app.models import Patient, Logs, Report, Activity
from django.db.models import Avg, Sum, F, fields, Count
from django.db.models.functions import Cast, Coalesce
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import permissions, status
from django.db import IntegrityError
from datetime import date
from django.db import transaction
from django.db.models import Value

class CreateReports(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        patients = Patient.objects.all()

        for patient in patients:
            logs = Logs.objects.filter(id_session__id_patient__user_id__user_id=patient.user_id.user_id)
            for log in logs:
                print('Vamos a ver que es este log', log)
            # Reemplazar valores None o no numéricos por cero
            logs = logs.annotate(
                tiempo_total=Coalesce(
                    Cast(F('log__tiempo_total'), output_field=fields.FloatField()),
                    Value(0)
                ),
                tiempo_rondas=Coalesce(
                    Cast(F('log__tiempo_rondas'), output_field=fields.FloatField()),
                    Value(0)
                ),
                errores=Coalesce(
                    Cast(F('log__errores'), output_field=fields.FloatField()),
                    Value(0)
                ),
                number_rondas=Coalesce(
                    Cast(F('log__number_rondas'), output_field=fields.FloatField()),
                    Value(0)
                )
            )

            with transaction.atomic():
                try:
                    # Crear un nuevo informe para el paciente
                    Report.objects.create(
                        patient=patient,
                        total_played_time=logs.aggregate(
                            total_played_time_sum=Sum(Cast(F('tiempo_total'), output_field=fields.FloatField()))
                        ).get('total_played_time_sum', 0),
                        avg_round_time=logs.aggregate(
                            avg_round_time_avg=Avg(Cast(F('tiempo_rondas'), output_field=fields.FloatField()))
                        ).get('avg_round_time_avg', 0),
                        total_errors=logs.aggregate(
                            total_errors_sum=Sum(Cast(F('errores'), output_field=fields.FloatField()))
                        ).get('total_errors_sum', 0),
                        total_rounds_played=logs.aggregate(
                            total_rounds_played_sum=Sum(Cast(F('number_rondas'), output_field=fields.FloatField()))
                        ).get('total_rounds_played_sum', 0),
                        total_games_played=logs.count()
                    )

                except IntegrityError as e:
                    # Si hay algún error de integridad (como valores nulos), manejarlo aquí
                    print(f"Error al crear el informe para el paciente {patient.name}: {e}")

        return HttpResponse('Reportes creados para todos los pacientes actualmente existentes')

class ReportRetreiveAPI(APIView):
    def get(self, request):
        reports_detailed  = Report.objects.all()
        result = []
        for report in reports_detailed:
            report_data = {
                'id': report.id,
                'date_created': report.date_created,
                'patient_id': report.patient.user_id.user_id,
                'patient_name': report.patient.name,
                'patient_lastname': report.patient.lastname,
                'patient_picture': report.patient.user_id.user_picture,
                'patient_parkinson_phase' : report.patient.id_parkinson_phase.id,
                'total_played_time': report.total_played_time,
                'avg_round_time': report.avg_round_time,
                'total_errors': report.total_errors,
                'total_rounds_played': report.total_rounds_played,
                'total_games_played': report.total_games_played
            }
            result.append(report_data)
        return Response(result)



class GetReportsByTherapistDetailed(APIView):
    def get(self, request, id_therapist):
        reports_detailed = Report.objects.filter(patient__id_therapist__user_id = id_therapist)
        result = []
        for report in reports_detailed:
            report_data = {
                'id': report.id,
                'date_created': report.date_created,
                'patient_id': report.patient.user_id.user_id,
                'patient_name': report.patient.name,
                'patient_lastname': report.patient.lastname,
                'patient_gender': report.patient.gender,
                'patient_picture': report.patient.user_id.user_picture,
                'patient_parkinson_phase' : report.patient.id_parkinson_phase.id,
                'total_played_time': report.total_played_time,
                'avg_round_time': report.avg_round_time,
                'total_errors': report.total_errors,
                'total_rounds_played': report.total_rounds_played,
                'total_games_played': report.total_games_played
            }

            result.append(report_data)
        return Response(result)

class GetStatsByTherapistDetailed(APIView):
    def get(self, request, id_therapist):
        activities_all = Activity.objects.filter(id_therapist__user_id = id_therapist)

        ## Total de actividades
        total_activities = activities_all.count()

        ## Total de actividades pendientes
        total_activities_pending = activities_all.filter(status = 'Pendiente').count()

        ## Total de actividades en curso
        total_activities_in_progress = activities_all.filter(status = 'En curso').count()

        ## Total de actividades terminadas
        total_activities_finished = activities_all.filter(status = 'Realizada').count()

        ## Total de actividades caducadas
        total_activities_lost = activities_all.filter(status = 'Caducado').count()


        response_data = {
            'total_activities': total_activities,
            'total_activities_pending': total_activities_pending,
            'total_activities_in_progress': total_activities_in_progress,
            'total_activities_finished': total_activities_finished,
            'total_activities_lost': total_activities_lost
        }

        return Response(response_data, status =status.HTTP_200_OK)

class GetReportsByPatientDetailed(APIView): 
     def get(self, request, id_patient):
        reports_detailed = Report.objects.filter(patient__user_id__user_id = id_patient)
        result = []
        for report in reports_detailed:
            report_data = {
                'id': report.id,
                'date_created': report.date_created,
                'patient_id': report.patient.user_id.user_id,
                'patient_name': report.patient.name,
                'patient_lastname': report.patient.lastname,
                'patient_gender': report.patient.gender,
                'patient_picture': report.patient.user_id.user_picture,
                'patient_parkinson_phase' : report.patient.id_parkinson_phase.id,
                'total_played_time': report.total_played_time,
                'avg_round_time': report.avg_round_time,
                'total_errors': report.total_errors,
                'total_rounds_played': report.total_rounds_played,
                'total_games_played': report.total_games_played
            }

            result.append(report_data)
        return Response(result)
     
class GetStatsByPatientDetailed(APIView):
     def get(self, request, id_patient):
        activities_all = Activity.objects.filter(id_patient__user_id = id_patient)

        ## Total de actividades
        total_activities = activities_all.count()

        ## Total de actividades pendientes
        total_activities_pending = activities_all.filter(status = 'Pendiente').count()

        ## Total de actividades en curso
        total_activities_in_progress = activities_all.filter(status = 'En curso').count()

        ## Total de actividades terminadas
        total_activities_finished = activities_all.filter(status = 'Realizada').count()

        ## Total de actividades caducadas
        total_activities_lost = activities_all.filter(status = 'Caducada').count()


        response_data = {
            'total_activities': total_activities,
            'total_activities_pending': total_activities_pending,
            'total_activities_in_progress': total_activities_in_progress,
            'total_activities_finished': total_activities_finished,
            'total_activities_lost': total_activities_lost
        }

        return Response(response_data, status =status.HTTP_200_OK)
     

class DeleteReportApi(DestroyAPIView):
    serializer_class = ReportSerializer
    model = Report
    permission_classes = [permissions.AllowAny]
    queryset = Report.objects.all()

    def delete(self, request, pk, format = None):
        Report = self.get_object()
        Report.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
