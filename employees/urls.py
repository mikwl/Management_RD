from django.urls import path

from .views import EmployeeListCreateView
urlpatterns = [

    path("employee/", EmployeeListCreateView.as_view()),
]