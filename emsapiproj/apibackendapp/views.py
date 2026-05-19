from rest_framework import viewsets, status, permissions
from .serializers import LoginSerializer, SignupSerializer, DepartmentSerializer, EmployeeSerializer, ProjectsSerializer, UserDetailsSerializer, UserSerializer
from .models import Department, Employee, Projects, UserDetails
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# Create your views here.

# APIview for signup
class SignupApIView(APIView):
    permission_classes = [] # to allow any user to access this view without authentication
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "user_id": user.id,
                "username": user.username,
                "token": token.key,
                "role": user.groups.all()[0].id if user.groups.exists() else None
            }, status=status.HTTP_201_CREATED)
        else:
            response = {'status':status.HTTP_400_BAD_REQUEST, 'data':serializer.errors}
            return Response(response,status=status.HTTP_400_BAD_REQUEST)

# Login API view
class LoginAPIview(APIView):
    permission_classes = []

    def post(self, request):
        serialiser = LoginSerializer(data=request.data)
        if serialiser.is_valid():
            username = serialiser.validated_data['username']
            password = serialiser.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                token = Token.objects.get_or_create(user=user)
                response = {
                    "status": status.HTTP_200_OK,
                    "message": "Login successful",
                    "username": user.username,
                    "role": user.groups.all()[0].id if user.groups.exists() else None,
                    "data": {
                        "Token": token.key
                    }
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "message": "Invalid username or password",
                }
                return Response(response, status=status.HTTP_401_UNAUTHORIZED)
        else:
            response = {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Invalid data",
                "data": serialiser.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

# Department view using ModelViewSet class
class DepartmentViewSet(viewsets.ModelViewSet):
    # Define a queryset (fields to be queried from model)
    queryset = Department.objects.all()
    # Define a serializer class
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # Bypass the authentication just in case for testing purpose, we will remove it later
     # permission_classes = [] # to bypass the authentication for testing purpose, we will remove it later



class UserDetailsViewSet(viewsets.ModelViewSet):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer