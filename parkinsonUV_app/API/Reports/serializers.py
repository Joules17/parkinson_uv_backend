from rest_framework import serializers
from parkinsonUV_app.models import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'date_created', 'patient', 'total_played_time', 'avg_round_time', 'total_errors', 'total_rounds_played', 'total_games_played']
