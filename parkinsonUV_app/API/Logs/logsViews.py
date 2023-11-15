from rest_framework.generics import UpdateAPIView, CreateAPIView,  ListAPIView, RetrieveAPIView, DestroyAPIView
from .serializers import ( 
    LogsSerializer, 
    LogsSerializerWithoutPK,
    LogSerializerWithGameData
)

from parkinsonUV_app.models import Session, Game_list, Logs
from rest_framework.response import Response
from rest_framework import permissions, status

class LogsCreateAPI(CreateAPIView):
    serializer_class = LogsSerializer
    model = Logs
    permission_classes = [permissions.AllowAny]

    def post(self, request): 
        session = Session.objects.get(id = request.data['id_session'])
        game_list = Game_list.objects.get(id = request.data['id_game_list'])
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save(id_session = session)
            serializer.save(id_game_list = game_list)
            return Response({'message' : '¡La Sesión fue creada con exito!'})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class LogsUpdateAPI(UpdateAPIView):
    serializer_class = LogsSerializerWithoutPK
    permission_classes = [permissions.AllowAny]
    queryset = Logs.objects.all()

class LogsRetreiveAPI(RetrieveAPIView):
    serializer_class = LogsSerializer
    model = Logs
    permission_classes = [permissions.AllowAny]
    queryset = Logs.objects.all()

class RetreiveAllLogs(ListAPIView):
    serializer_class = LogsSerializer
    model = Logs
    permission_classes = [permissions.AllowAny]
    queryset = Logs.objects.all()

class DeleteLogsAPI(DestroyAPIView):
    serializer_class = LogsSerializer
    model = Logs
    permission_classes = [permissions.AllowAny]
    queryset = Logs.objects.all()

    def delete(self, request, pk, format = None):
        Logs = self.get_object()
        Logs.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
class LogsBySessionAPI(ListAPIView):
    serializer_class = LogSerializerWithGameData  # Asegúrate de tener un serializer adecuado para Logs
    queryset = Logs.objects.all()

    def get_queryset(self):
        id_session = self.kwargs['id_session']
        queryset = Logs.objects.filter(id_session=id_session)
        return queryset
