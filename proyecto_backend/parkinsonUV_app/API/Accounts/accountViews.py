from rest_framework.generics import UpdateAPIView, CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import (
    AccountSerializer, 
    AccountAuthSerializer, 
    RetreivePatientAccountSerializer, 
    RetreiveTherapistAccountSerializer, 
    ActivationAccountSerializer
)

from parkinsonUV_app.models import Account, Patient, Therapist
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView

import http.client
import json, os
from dotenv import load_dotenv

class AccountCreateApi(CreateAPIView): 
    serializer_class = AccountSerializer
    model = Account
    permission_classes = [permissions.AllowAny]

class AccountUpdateApi(UpdateAPIView): 
    serializer_class = AccountSerializer
    model = Account
    permission_classes = [permissions.AllowAny]
    queryset = Account.objects.all()

class AccountRetrieveApi(RetrieveAPIView): 
    serializer_class = AccountSerializer
    model = Account
    permission_classes = [permissions.AllowAny]
    queryset = Account.objects.all()

class RetreiveAllAccounts(ListAPIView): 
    serializer_class = AccountSerializer
    model = Account
    permission_classes = [permissions.AllowAny]
    queryset = Account.objects.all()

class ActivationAPI(UpdateAPIView): 
    serializer_class = ActivationAccountSerializer
    model = Account
    permission_classes = [permissions.AllowAny]
    queryset = Account.objects.all()

## Views detalladas 
class RetreiveAllPatientsDetailed(ListAPIView): 
    serializer_class = RetreivePatientAccountSerializer
    model = Patient
    permission_classes = [permissions.AllowAny]
    queryset = Patient.objects.all()

class RetreiveAllTherapistDetailed(ListAPIView): 
    serializer_class = RetreiveTherapistAccountSerializer
    model = Therapist
    permission_classes = [permissions.AllowAny]
    queryset = Therapist.objects.all()