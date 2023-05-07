from rest_framework.generics import UpdateAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
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

class AccountAuthRetreiveApi(APIView): 
    serializer_class = AccountAuthSerializer
    permission_classes = [permissions.AllowAny]
    def post (self, request): 
        user_id = request.data['user_id']
        cuenta = Account.objects.filter(user_id = user_id).first()

        ## Cuenta no registrada = 0
        if (not(cuenta is None)): 
            id_type = 0
        
        ## Cuenta que no debe ser registrada (ya existe)
        else: 
            id_type = 3
        user_status = True
        
        return Response({'authdata': 'no hay', 'user_id' : user_id, 'id_type': id_type, 'user_status': user_status, 'token': 'no hay token'})
    
class DeleteAccountApi(DestroyAPIView): 
    serializer_class = AccountSerializer
    model = Account 
    permission_classes = [permissions.AllowAny]
    queryset = Account.objects.all()

    def delete(self, request, pk, format= None): 
        account = self.get_object()
        account.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

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