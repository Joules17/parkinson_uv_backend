from .serializers import ReportSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from parkinsonUV_app.models import Patient, Logs, Report
from django.db.models import Avg, Sum, Q, F, ExpressionWrapper, fields, Count
from django.db.models.functions import Cast
from django.http import HttpResponse
from rest_framework import permissions
from django.db import IntegrityError
from datetime import date
from django.db import transaction
from django.db.models import Value

class CreateReports(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request): 
        patients = Patient.objects.all(); 

        for patient in patients:
            logs = Logs.objects.filter(id_session__id_patient__user_id__user_id=str(patient.user_id.user_id))
            print('QUIERO VER ESE QUERY', logs.query)
            # Filtrar logs "malos"
            logs = logs.exclude(
                Q(log__errores_isNumeric=False) |
                Q(log__tiempo_total__isnumeric=False) |
                Q(log__number_rondas__isnumeric=False) |
                Q(log__tiempo_rondas__isnumeric=False) 
            )

            ## HACER EL PRINT JUSTO AQUI DE LOS ELEMENTOS ERRORES TIEMPO TOTAL NUMBER RONDAS Y TIEMPO RONDAS DE CADA LOG
            print('HOLA BEBIBIIII******************************************** TAMAÑO DE LOG:', len(logs), ' VAMOS A VER LOS HUEVOS DE ESE PACIENTE ', patient.name, patient.user_id.user_id)
            for log in logs: 
                print('Hola, esto es un aviso informativo del paciente', patient.name, 'y el log', log.id, 'y sus errores son', log.log.errores, 'y su tiempo total es', log.log.tiempo_total, 'y su numero de rondas es', log.log.number_rondas, 'y su tiempo de rondas es', log.log.tiempo_rondas)
            
            with transaction.atomic():
                try:
                    # Crear un nuevo informe para el paciente
                    Report.objects.create(
                        patient=patient,
                        total_played_time=logs.aggregate(
                            total_played_time_sum=Sum(
                                Cast(F('log__tiempo_total__item__tiempo_total'), output_field=fields.FloatField())
                            )
                        ).get('total_played_time_sum', 0),
                        avg_round_time=logs.aggregate(
                            avg_round_time_avg=Avg(
                                Cast(F('log__tiempo_rondas'), output_field=fields.FloatField())
                            )
                        ).get('avg_round_time_avg', 0),
                        total_errors=logs.aggregate(
                            total_errors_sum=Sum(
                                Cast(F('log__errores'), output_field=fields.FloatField())
                            )
                        ).get('total_errors_sum', 0),
                        total_rounds_played=logs.aggregate(
                            total_rounds_played_sum=Sum(
                                Cast(F('log__number_rondas'), output_field=fields.FloatField())
                            )
                        ).get('total_rounds_played_sum', 0),
                        total_games_played=logs.count()
                    )

                except IntegrityError as e:
                    # Si hay algún error de integridad (como valores nulos), manejarlo aquí
                    print(f"Error al crear el informe para el paciente {patient.name}: {e}")

        return HttpResponse('Reportes creados para todos los pacientes actualmente existentes')

class ReportRetreiveAPI(ListAPIView): 
    serializer_class = ReportSerializer
    model = Report
    permission_classes = [permissions.AllowAny]
    queryset = Report.objects.all()