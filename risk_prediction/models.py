from django.db import models

class Factors(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    age = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    heart_rate = models.IntegerField()
    is_smoking = models.BooleanField()
    cigarets_per_day = models.IntegerField()
    blood_pressure_medicines = models.BooleanField()
    stroke = models.BooleanField()
    hypertension = models.BooleanField()
    diabetes = models.BooleanField()
    systolic_blood_pressure = models.FloatField()
    diastolic_blood_pressure = models.FloatField()


class Prediction(models.Model):
    # factors_batch = models.ForeignKey(Factors, on_delete=models.CASCADE, related_name='prediction')
    risk_value = models.FloatField()