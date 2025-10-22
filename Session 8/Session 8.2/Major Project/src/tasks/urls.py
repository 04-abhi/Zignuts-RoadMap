from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, MyTokenObtainPairView, TaskViewSet
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    # API URLs
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),  # /api/tasks/
    
    # Template URLs
    path('login-page/', views.login_page),
    path('register-page/', views.register_page),
    path('dashboard-page/', views.dashboard_page),
]
