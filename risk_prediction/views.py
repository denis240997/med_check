from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from risk_prediction import serializers
from risk_prediction.prediction_model import predict_risk


@api_view(['POST'])
def get_prediction(request, format=None):
    
    if request.method == 'POST':
        serializer = serializers.FactorsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        response_data = {
            'prediction': predict_risk(data)
        }
        return Response(response_data, status.HTTP_200_OK)