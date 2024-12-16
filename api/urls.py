from rest_framework.routers import DefaultRouter
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include
from .views import UserViewSet, ProjectViewSet, TaskViewSet, CommentViewSet,ProjectMemberViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'project-members', ProjectMemberViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Project Management API",
      default_version='v1',
      description="API documentation for the project management tool",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@projectmanagement.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
