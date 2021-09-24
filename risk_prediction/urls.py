from django.urls import path
from risk_prediction import views

urlpatterns = [
    path('predict/', views.PostFactorsView.as_view(), name='predict'),
    path('prediction/<int:pk>/', views.GetPredictionView.as_view(), name='prediction'),
]