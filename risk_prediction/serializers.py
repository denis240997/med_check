from rest_framework import serializers

from risk_prediction import models


class FactorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Factors
        fields = '__all__'
