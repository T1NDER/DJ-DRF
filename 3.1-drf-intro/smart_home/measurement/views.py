from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, SensorListSerializer, MeasurementSerializer

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


class SensorListCreateView(ListCreateAPIView):
    """
    Обработчик для получения списка датчиков и создания нового датчика
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SensorDetailSerializer
        return super().get_serializer_class()

class SensorRetrieveUpdateView(RetrieveUpdateAPIView):
    """
    Обработчик для просмотра, обновления и частичного обновления датчика
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasurementCreateView(CreateAPIView):
    """
    Обработчик для создания нового измерения
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def perform_create(self, serializer):
        sensor_id = self.request.data.get('sensor')
        sensor = Sensor.objects.get(pk=sensor_id)
        serializer.save(sensor=sensor)