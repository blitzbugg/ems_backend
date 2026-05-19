from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DepartmentSerializer, EmployeeSerializer, ProjectsSerializer, UserDetailsSerializer, UserSerializer
from .models import Department, Employee, Projects, UserDetails
from django.contrib.auth.models import User, Group
# Create your views here.

# Department view using ModelViewSet class
class DepartmentViewSet(viewsets.ModelViewSet):
    # Define a queryset (fields to be queried from model)
    queryset = Department.objects.all()
    # Define a serializer class
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class UserDetailsViewSet(viewsets.ModelViewSet):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer