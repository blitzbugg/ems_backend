from django.contrib import admin

# Register your models here.
# import all models from the models.py file
from .models import Department, Employee, UserDetails, Projects
# register the models in the admin site
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(UserDetails)
admin.site.register(Projects)

