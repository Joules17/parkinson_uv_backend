"""proyecto_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

## Cuentas: 
from parkinsonUV_app.API.Accounts.accountViews import (
    AccountCreateApi, 
    AccountUpdateApi, 
    AccountRetrieveApi, 
    RetreiveAllAccounts
)

## Terapeutas: 
from parkinsonUV_app.API.Therapist.therapistViews import (
    TherapistCreateApi, 
    TherapistUpdateApi, 
    TherapistRetrieveApi, 
    RetreiveAllTherapists
)

## Pacientes: 
from parkinsonUV_app.API.Patients.patientsViews import (
    PatientCreateApi, 
    PatientUpdateApi, 
    PatientRetrieveApi, 
    RetreiveAllPatients
)

urlpatterns = [
    path('admin/', admin.site.urls),
    ## Accounts ----------------------------------------------------------------------------
    path('api/account/create', AccountCreateApi.as_view()), 
    path('api/account/update/<str:pk>', AccountUpdateApi.as_view()), 
    path('api/account/retreive/<str:pk>', AccountRetrieveApi.as_view()), 
    path('api/account/retreive/all', RetreiveAllAccounts.as_view()), 
    ## Therapists ----------------------------------------------------------------------------
    path('api/therapist/create', TherapistCreateApi.as_view()),
    path('api/therapist/update/<str:pk>', TherapistUpdateApi.as_view()),
    path('api/therapist/retrieve/<str:pk>', TherapistRetrieveApi.as_view()),
    path('api/therapist/retreive/all', RetreiveAllTherapists.as_view()),
    ## Patients  ----------------------------------------------------------------------------
    path('api/patient/create', PatientCreateApi.as_view()),
    path('api/patient/update/<str:pk>', PatientUpdateApi.as_view()),
    path('api/patient/retrieve/<str:pk>', PatientRetrieveApi.as_view()),
    path('api/patient/retreive/all', RetreiveAllPatients.as_view()),
]
