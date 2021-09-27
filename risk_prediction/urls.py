from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from risk_prediction import views

urlpatterns = [
    path('predict/', views.get_prediction, name='predict'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
