from django.urls import path
from . import views


urlpatterns = [
    path('', views.EmployeeListAPIView.as_view()),
    path('drf/', views.EmployeeDRFListAPIView.as_view()),
]
