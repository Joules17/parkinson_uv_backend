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
    DeleteAccountApi,
    AccountUpdateStatusApi
)

## Terapeutas:
from parkinsonUV_app.API.Therapist.therapistViews import (
    TherapistCreateApi,
    TherapistUpdateApi,
    getTherapistDetailed,
    TherapistRetrieveApi,
    RetreiveAllTherapists
)

## Pacientes:
from parkinsonUV_app.API.Patients.patientsViews import (
    PatientCreateApi,
    PatientUpdateApi,
    PatientUpdateAssigneeApi,
    PatientRetrieveApi,
    GetPatientDetailed,
    RetreiveAllPatients,
    RetreiveTherapistPatients
)

## Juegos:
from parkinsonUV_app.API.Games.gamesViews import (
    ## Games
    GameCreateApi,
    GameUpdateApi,
    GameRetreiveApi,
    RetreiveAllGames,
    RetreiveAllGamesWithType,
    DeleteGameApi,
    ## GameTypes
    GameTypeCreateApi,
    GameTypeUpdateApi,
    GameTypeRetreiveApi,
    RetreiveAllGameTypes,
    DeleteGameTypeApi
)

# Lista de juegos
from parkinsonUV_app.API.ListGames.listGamesViews import (
    ListCreateApi,
    ListUpdateApi,
    ListRetreiveApi,
    RetreiveAllList,
    RetreiveTherapistLists,
    DeleteListApi,
    CheckListInActivity,
    MarkGameAsPlayed,

    GameListCreateApi,
    GameListUpdateApi,
    GameListRetreiveApi,
    RetreiveAllGameList,
    DeleteGameListApi,
    GameListSettingUpdateApi
)

## Parkinson_phase
from parkinsonUV_app.API.ParkinsonPhase.parkinsonPhaseViews import (
    ParkinsonCreateApi,
    ParkinsonUpdateApi,
    ParkinsonRetrieveApi,
    RetreiveAllParkinsons,
    DeleteParkinsonApi
)

## Actividades
from parkinsonUV_app.API.Activity.activityViews import (
    ActivityCreateAPI,
    ActivityRetreiveAPI,
    ActivityUpdateAPI,
    RetreiveAllActivities,
    UpdateActivitiesStatus,
    DeleteActivityApi,
    GetActivitiesByTherapistDetailed,
    GetActivitiesByPatientDetailed,
    ActivityStatusUpdateAPI,
)

## Sessions
from parkinsonUV_app.API.Sessions.sessionsViews import (
    SessionCreateAPI,
    SessionRetreiveAPI,
    SessionUpdateAPI,
    RetreiveAllSessions,
    DeleteSessionAPI,
    SessionIdView,
    GetSessionsByTherapistDetailed,
)

## Logs
from parkinsonUV_app.API.Logs.logsViews import (
    LogsCreateAPI,
    LogsRetreiveAPI,
    LogsUpdateAPI,
    RetreiveAllLogs,
    DeleteLogsAPI,
    LogsBySessionAPI
)

app_name = 'parkinsonUV_app'
from parkinsonUV_app.API.Reports.reportsViews import (
    CreateReports,
    ReportRetreiveAPI,
    DeleteReportApi,
    GetReportsByTherapistDetailed,
    GetStatsByTherapistDetailed, 
    GetReportsByPatientDetailed, 
    GetStatsByPatientDetailed
)

urlpatterns = [
    path('admin/', admin.site.urls),
    ## Auth --------------------------------------------------------------------------------
    path('api/auth/retrieve', AccountAuthRetreiveApi.as_view()),
    ## Accounts ----------------------------------------------------------------------------
    path('api/account/create', AccountCreateApi.as_view(), name='account-create'),
    path('api/account/update/<str:pk>', AccountUpdateApi.as_view(), name='account-update'),
    path('api/account/retreive/<str:pk>', AccountRetrieveApi.as_view(), name='account-retrieve'),
    path('api/account/retreive/', RetreiveAllAccounts.as_view(), name='account-retrieve-all'),
    path('api/account/delete/<str:pk>', DeleteAccountApi.as_view(), name='account-delete'),
    path('api/account/update/status/<str:pk>', AccountUpdateStatusApi.as_view(), name='account-update-status'),
    ## Therapists ----------------------------------------------------------------------------
    path('api/therapist/create', TherapistCreateApi.as_view(), name='therapist-create'),
    path('api/therapist/update/<str:pk>', TherapistUpdateApi.as_view(), name='therapist-update'),
    path('api/therapist/retreive/<str:pk>', TherapistRetrieveApi.as_view(), name='therapist-retrieve'),
    path('api/therapist/retreive/detailed/<str:user_id>', getTherapistDetailed.as_view(), name='therapist-retrieve-detailed'),
    path('api/therapist/retreive/', RetreiveAllTherapists.as_view(), name='therapist-retrieve-all'),
    ## Patients  ----------------------------------------------------------------------------
    path('api/patient/create', PatientCreateApi.as_view(), name='patient-create'),
    path('api/patient/update/<str:pk>', PatientUpdateApi.as_view()),
    path('api/patient/update/assignee/<str:pk>', PatientUpdateAssigneeApi.as_view()),
    path('api/patient/retreive/<str:pk>', PatientRetrieveApi.as_view()),
    path('api/patient/retreive/detailed/<str:user_id>', GetPatientDetailed.as_view()),
    path('api/patient/retreive/', RetreiveAllPatients.as_view(), name='patient-retrieve-all'),
    path('api/patient/retreive/therapist/<str:id_therapist>/', RetreiveTherapistPatients.as_view()),
    ## Games --------------------------------------------------------------------------------
    path('api/game/create', GameCreateApi.as_view()),
    path('api/game/update/<str:pk>', GameUpdateApi.as_view()),
    path('api/game/retreive/<str:pk>', GameRetreiveApi.as_view()),
    path('api/game/retreive/', RetreiveAllGamesWithType.as_view(), name='game-retrieve-all'),
    path('api/game/delete/<str:pk>', DeleteGameApi.as_view()),
    ## Game_Type ----------------------------------------------------------------------------
    path('api/game_type/create', GameTypeCreateApi.as_view()),
    path('api/game_type/update/<str:pk>', GameTypeUpdateApi.as_view()),
    path('api/game_type/retreive/<str:pk>', GameTypeRetreiveApi.as_view()),
    path('api/game_type/retreive/', RetreiveAllGameTypes.as_view(), name='game-type-retrieve-all'),
    path('api/game_type/delete/<str:pk>', DeleteGameTypeApi.as_view()),
    ## Parkinson Phases ---------------------------------------------------------------------
    path('api/parkinson/create', ParkinsonCreateApi.as_view()),
    path('api/parkinson/update/<str:pk>', ParkinsonUpdateApi.as_view()),
    path('api/parkinson/retreive/<str:pk>', ParkinsonRetrieveApi.as_view()),
    path('api/parkinson/retreive/', RetreiveAllParkinsons.as_view(), name='parkinson-retrieve-all'),
    path('api/parkinson/delete/<str:pk>', DeleteParkinsonApi.as_view()),
    ## Games List ---------------------------------------------------------------------------
    path('api/game_list/create', GameListCreateApi.as_view()),
    path('api/game_list/update/<int:pk>', GameListUpdateApi.as_view()),
    path('api/game_list/update/setting/<int:pk>', GameListSettingUpdateApi.as_view()),
    path('api/game_list/retreive/<str:pk>', GameListRetreiveApi.as_view()),
    path('api/game_list/retreive/', RetreiveAllGameList.as_view()),
    path('api/game_list/delete/<str:pk>', DeleteGameApi.as_view()),
    ## List ---------------------------------------------------------------------------------
    path('api/list/create', ListCreateApi.as_view()),
    path('api/list/update/<str:pk>', ListUpdateApi.as_view()),
    path('api/list/retreive/<str:pk>', ListRetreiveApi.as_view()),
    path('api/list/retreive/therapist/<str:id_therapist>/', RetreiveTherapistLists.as_view()),
    path('api/list/retreive/', RetreiveAllList.as_view(), name='create-list'),
    path('api/list/delete/<str:pk>', DeleteListApi.as_view()),
    path('api/list/check/<str:pk>', CheckListInActivity.as_view()),
    path('api/list/game/played/<str:id_list>/<str:id_game_list>', MarkGameAsPlayed.as_view(), name='mark-game-as-played'),
    ## Activities ---------------------------------------------------------------------------
    path('api/activity/create', ActivityCreateAPI.as_view()),
    path('api/activity/update/<str:pk>', ActivityUpdateAPI.as_view()),
    path('api/activity/retreive/<str:pk>', ActivityRetreiveAPI.as_view()),
    path('api/activity/retreive/', RetreiveAllActivities.as_view(), name='create-activity'),
    path('api/activity/delete/<str:pk>', DeleteActivityApi.as_view()),
    path('api/activity/retreive/therapist/<str:id_therapist>/', GetActivitiesByTherapistDetailed.as_view()),
    path('api/activity/retreive/patient/<str:id_patient>/', GetActivitiesByPatientDetailed.as_view()),
    path('api/activity/statuses', UpdateActivitiesStatus.as_view()),
    path('api/activity/update/status/<str:pk>', ActivityStatusUpdateAPI.as_view()),

    ## Sessions -----------------------------------------------------------------------------
    path('api/session/create', SessionCreateAPI.as_view()),
    path('api/session/update/<str:pk>', SessionUpdateAPI.as_view()),
    path('api/session/retreive/<str:pk>', SessionRetreiveAPI.as_view()),
    path('api/session/retreive/', RetreiveAllSessions.as_view(), name='create-session'),
    path('api/session/delete/<str:pk>', DeleteSessionAPI.as_view()),
    path('api/session/getId/<int:id_activity>/<str:id_patient>', SessionIdView.as_view()),
    path('api/session/retreive/therapist/<str:id_therapist>/', GetSessionsByTherapistDetailed.as_view()),
    ## Logs -----------------------------------------------------------------------------
    path('api/logs/create', LogsCreateAPI.as_view()),
    path('api/logs/delete/<str:pk>', DeleteLogsAPI.as_view()),
    path('api/logs/retreive/', RetreiveAllLogs.as_view()),
    path('api/logs/session/<int:id_session>', LogsBySessionAPI.as_view()),
    ## Reports -----------------------------------------------------------------------------
    path('api/reports/create', CreateReports.as_view()),
    path('api/reports/retreive/', ReportRetreiveAPI.as_view()),
    path('api/reports/delete/<str:pk>', DeleteReportApi.as_view()),
    path('api/reports/retreive/therapist/<str:id_therapist>/', GetReportsByTherapistDetailed.as_view()),
    path('api/reports/stats/therapist/<str:id_therapist>/', GetStatsByTherapistDetailed.as_view()),
    path('api/reports/retreive/patient/<str:id_patient>/', GetReportsByPatientDetailed.as_view()),
    path('api/reports/stats/patient/<str:id_patient>/', GetStatsByPatientDetailed.as_view()),
]
