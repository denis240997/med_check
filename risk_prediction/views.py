from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from risk_prediction import models, serializers


class PostFactorsView(CreateAPIView):
    serializer_class = serializers.FactorsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)

        prediction = models.Prediction.objects.create(risk_value=58)

        headers = self.get_success_headers(serializer.data)
        return redirect(f'/api/prediction/{prediction.pk}/')
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# class GetPredictionView(RetrieveAPIView):
#     serializer_class = serializers.PredictionSerializer

#     def get_object(self, pk):
#         queryset = self.get_queryset()
#         filter = {}
#         for field in self.multiple_lookup_fields:
#             filter[field] = self.kwargs[field]

#         obj = get_object_or_404(queryset, **filter)
#         self.check_object_permissions(self.request, obj)
#         return obj

class GetPredictionView(APIView):

    def get_object(self, pk):
        try:
            return models.Prediction.objects.get(pk=pk)
        except models.Prediction.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prediction = self.get_object(pk)
        serializer = serializers.PredictionSerializer(prediction)
        return Response(serializer.data)



# @csrf_exempt
# def get_prediction(request):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = serializers.FactorsSerializer(data=data)
#         if serializer.is_valid():
#             # serializer.save()
#             res = {'sosi': 'pisos'}
#             return JsonResponse(res, status=201)
#         return JsonResponse(serializer.errors, status=400)

#     # else:
#     #     return Http404('Bad request!')
