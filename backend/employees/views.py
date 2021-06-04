from rest_framework.generics import ListAPIView
from .serializers import *
from .models import Employee


class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
