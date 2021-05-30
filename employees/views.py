from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.generics import ListCreateAPIView


class EmployeeListCreateView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer