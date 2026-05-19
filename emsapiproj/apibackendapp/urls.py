from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'userdetails', views.UserDetailsViewSet)
router.register(r'projects', views.ProjectsViewSet)

# Add all the generated urls to urlpatterns
urlpatterns = router.urls