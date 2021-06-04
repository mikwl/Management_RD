from django.urls import path
from .views import *

app_name = "employees"

urlpatterns = [path("user/", EmployeeListView.as_view()),
]