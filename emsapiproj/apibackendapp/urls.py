from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

router = DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'userdetails', views.UserDetailsViewSet)
router.register(r'projects', views.ProjectsViewSet)

# Add all the generated urls to urlpatterns

urlpatterns = [
    path('signup/', views.SignupApIView.as_view(), name='signup'),
    path('login/', views.LoginAPIview.as_view(), name='login'),
]

urlpatterns += router.urls