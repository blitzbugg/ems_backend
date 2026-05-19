from rest_framework import serializers
# Import all the models from the current directory's models.py file.
from .models import Department, Employee, Projects,UserDetails

from django.contrib.auth.models import User

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        # To provide meta data to the serializer, class whwre we specify the model and fields to be serialized.
        model = Department
        fields = ('DepartmentID', 'DepartmentName') # we can also use fields = '__all__' to serialize all the fields of the model but it is not a good practice to use it because it will serialize all the fields of the model which may not be required in the API response.
    
class EmployeeSerializer(serializers.ModelSerializer):
    # 
    Department = DepartmentSerializer(source='DepartmentId', read_only=True) # to get the department details in the employee details, we need to use the source parameter to specify the field which is the foreign key in the employee model and read_only to make it read only field because we don't want to update the department details from the employee details.

    projects = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(), many=True, required=False, write_only=True)

    

    projects_details = serializers.StringRelatedField(read_only=True, many=True, source='projects') # to get the project details in the employee details, we need to use the source parameter to specify the field which is the many to many field in the employee model and many to true because it is a many to many field and required false because we don't want to make it a required field in the employee details.
    class Meta:
        model = Employee
        # using the Department details obtained, create a nested json field in the dept details
        fields = ('EmployeeID', 'EmployeeName', 'Designation', 'Contact', 'DateOfJoining', 'DepartmentId', 'IsActive', 'Department', 'projects_details','projects') # we can also use fields = '__all__' to serialize all the fields of the model but it is not a good practice to use it because it will serialize all the fields of the model which may not be required in the API response.

class ProjectsSerializer(serializers.ModelSerializer):
    employee_details = EmployeeSerializer(source='employees', many=True, read_only=True,required=False) # to get the employee details in the project details, we need to use the source parameter to specify the field which is the many to many field in the projects model and read_only to make it read only field because we don't want to update the employee details from the project details.
    class Meta:
        model = Projects
        fields = ('id', 'name', 'employees', 'employee_details')

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # default value for fields is '__all__' which means all the fields of the model will be serialized. we don't need that
        fields = ('id', 'username')

