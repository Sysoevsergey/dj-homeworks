from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, MeasurementDetailSerializer


class SensorView(APIView):

	def get(self, request):
		sensors = Sensor.objects.all()
		serializer = SensorSerializer(sensors, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = SensorSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SensorDetailView(APIView):

	def get_object(self, pk):
		try:
			return Sensor.objects.get(pk=pk)
		except Sensor.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

	def get(self, request, pk):
		sensor = self.get_object(pk)
		measurements = Measurement.objects.filter(sensor_id=pk)
		measurements_serializer = MeasurementDetailSerializer(measurements, many=True)
		data = {
			'id': sensor.id,
			'name': sensor.name,
			'description': sensor.description,
			'measurements': measurements_serializer.data
		}
		return Response(data)

	def patch(self, request, pk):
		sensor = self.get_object(pk)
		serializer = SensorSerializer(sensor, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		sensor = self.get_object(pk)
		sensor.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class MeasurementView(APIView):
	parser_classes = (MultiPartParser, FormParser)
	serializer = MeasurementSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.serializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
