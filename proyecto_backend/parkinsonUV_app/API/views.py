from rest_framework.generics import ListAPIView

from ..models import Therapist, Patient

from .serializers import TherapistSerializer, PatientSerializer

## Terapeutas 

class TherapistList(ListAPIView):
    queryset = Therapist.objects.all()
    serializer_class = TherapistSerializer


## Pacientes

class PatientList(ListAPIView): 
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer