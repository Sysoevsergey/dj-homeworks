from django.db import models


class Sensor(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=100)


class Measurement(models.Model):
	temperature = models.FloatField()
	sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE, default=1)
	image = models.ImageField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)


class MeasurementSensor(models.Model):
	sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
	measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name='measurements_sensor')
