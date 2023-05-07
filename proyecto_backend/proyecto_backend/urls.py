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
    RetreiveAllAccounts, 
    AccountAuthRetreiveApi, 
    DeleteAccountApi
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

## Juegos: 
from parkinsonUV_app.API.Games.gamesViews import (
    ## Games 
    GameCreateApi, 
    GameUpdateApi, 
    GameRetreiveApi, 
    RetreiveAllGames, 
    DeleteGameApi,
    ## GameTypes
    GameTypeCreateApi, 
    GameTypeUpdateApi, 
    GameTypeRetreiveApi, 
    RetreiveAllGameTypes, 
    DeleteGameTypeApi
)

## Parkinson_phase
from parkinsonUV_app.API.ParkinsonPhase.parkinsonPhaseViews import (
    ParkinsonCreateApi, 
    ParkinsonUpdateApi, 
    ParkinsonRetrieveApi, 
    RetreiveAllParkinsons, 
    DeleteParkinsonApi
)

urlpatterns = [
    path('admin/', admin.site.urls),
    ## Auth --------------------------------------------------------------------------------
    path('api/auth/retrieve', AccountAuthRetreiveApi.as_view()),
    ## Accounts ----------------------------------------------------------------------------
    path('api/account/create', AccountCreateApi.as_view()), 
    path('api/account/update/<str:pk>', AccountUpdateApi.as_view()), 
    path('api/account/retreive/<str:pk>', AccountRetrieveApi.as_view()), 
    path('api/account/retreive/', RetreiveAllAccounts.as_view()), 
    path('api/account/delete/<str:pk>', DeleteAccountApi.as_view()), 
    ## Therapists ----------------------------------------------------------------------------
    path('api/therapist/create', TherapistCreateApi.as_view()),
    path('api/therapist/update/<str:pk>', TherapistUpdateApi.as_view()),
    path('api/therapist/retreive/<str:pk>', TherapistRetrieveApi.as_view()),
    path('api/therapist/retreive/', RetreiveAllTherapists.as_view()),
    ## Patients  ----------------------------------------------------------------------------
    path('api/patient/create', PatientCreateApi.as_view()),
    path('api/patient/update/<str:pk>', PatientUpdateApi.as_view()),
    path('api/patient/retreive/<str:pk>', PatientRetrieveApi.as_view()),
    path('api/patient/retreive/', RetreiveAllPatients.as_view()),
    ## Games --------------------------------------------------------------------------------
    path('api/game/create', GameCreateApi.as_view()), 
    path('api/game/update/<str:pk>', GameUpdateApi.as_view()),
    path('api/game/retreive/<str:pk>', GameRetreiveApi.as_view()), 
    path('api/game/retreive/', RetreiveAllGames.as_view()),
    path('api/game/delete/<str:pk>', DeleteGameApi.as_view()),
    ## Game_Type ----------------------------------------------------------------------------
    path('api/game_type/create', GameTypeCreateApi.as_view()), 
    path('api/game_type/update/<str:pk>', GameTypeUpdateApi.as_view()),
    path('api/game_type/retreive/<str:pk>', GameTypeRetreiveApi.as_view()), 
    path('api/game_type/retreive/', RetreiveAllGameTypes.as_view()),
    path('api/game_type/delete/<str:pk>', DeleteGameTypeApi.as_view()),
    ## Parkinson Phases ---------------------------------------------------------------------
    path('api/parkinson/create', ParkinsonCreateApi.as_view()), 
    path('api/parkinson/update/<str:pk>', ParkinsonUpdateApi.as_view()),
    path('api/parkinson/retreive/<str:pk>', ParkinsonRetrieveApi.as_view()), 
    path('api/parkinson/retreive/', RetreiveAllParkinsons.as_view()),
    path('api/parkinson/delete/<str:pk>', DeleteParkinsonApi.as_view()),
]
