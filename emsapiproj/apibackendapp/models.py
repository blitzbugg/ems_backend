from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.

class Department(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=200)

        # in django admin the object name is displayed instead of the class name, so we need to use a special fn called  __str__ it will print the name of the department instead of the object name in django admin

    def __str__(self):
        return self.DepartmentName
    
# create the Employee model
class Employee(models.Model):
    EmployeeID = models.AutoField(primary_key=True) #int
    EmployeeName = models.CharField(max_length=200) #string
    Designation = models.CharField(max_length=150) #string
    Contact = models.CharField(max_length=150) #string
    DateOfJoining = models.DateField() #date
    DepartmentId = models.ForeignKey(Department, on_delete=models.CASCADE) #foreign key  
    # cascade delete : department illathe employee illa!
    IsActive = models.BooleanField(default=True) #boolean

    def __str__(self):
        return self.EmployeeName

# UserDetails model

class UserDetails(models.Model):
    # get the user details from the builtin model of Django called User
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_details')
     # one to one relationship with the User model
     # related_name is used to access the user details from the user model, we can use user.user_details to access the user details of a user
    # also called as reverse relationship
    phoneno = models.CharField(max_length=50) #string
    email = models.EmailField() #string
    
    def __str__(self):
        return self.user.username
     
# create projects Model 
class Projects(models.Model):
    # project id is auto generated we will define the name
    name = models.CharField(max_length=200) #string
    # many to many relationship with the employee model
    employees = models.ManyToManyField(Employee, related_name='projects') # many to many relationship with the employee model
    def __str__(self):
        return self.name