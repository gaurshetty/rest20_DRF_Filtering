from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.generics import ListAPIView


# 1) Planin Vanilla Filtering:
class EmployeeListAPIView(ListAPIView):
    # queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        qs = Employee.objects.all()
        name = self.request.GET.get('name')
        if name is not None:
            qs = qs.filter(name__icontains=name)
        return qs


# 2) By using Django RestFramework API:
class EmployeeDRFListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    search_fields = ('name', '^no')
    ordering_fields = ('salary')


