from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from parkinsonUV_app.models import Patient, Logs, Report
from django.db.models import Avg, Sum 

class CreateReports(APIView):
    def generate_reports(): 
        patients = Patient.objects.all(); 
        
        for patient in patients:
            logs = Logs.object.filter(id_session__id_patient=patient)
            total_played_time = logs.aggregate(Sum('log__played_time'))['log__played_time__sum']
            avg_round_time = logs.aggregate(Avg('log__round_time'))['log__round_time__avg']
            total_errors = logs.aggregate(Sum('log__errors'))['log__errors__sum']
            total_games_played = logs.count()

            Report.objects.create(
                patient=patient,
                total_played_time=total_played_time,
                avg_round_time=avg_round_time,
                total_errors=total_errors,
                total_games_played=total_games_played
            )

class ReportRetreiveAPI(RetreiveApiView): 
    serializer_class = ReportSerializer
    model = Report
    permission_classes = [permissions.AllowAny]
    queryset = Report.objects.all()