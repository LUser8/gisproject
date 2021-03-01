from django.db import models
from django.contrib.auth.models import User


class FieldGrass(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class FarmerFields(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=100)
    grass_type = models.ForeignKey(FieldGrass, on_delete=models.CASCADE)
    grass_age = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=20)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.field_name


class FieldFlight(models.Model):
    field_name = models.ForeignKey(FarmerFields, on_delete=models.CASCADE)
    pilot_name = models.CharField(max_length=50)
    flight_time = models.TimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now_add=True)
    drone_data = models.FileField(default='field_default_data.zip', upload_to='drone_data')

    def __str__(self):
        return self.field_name
