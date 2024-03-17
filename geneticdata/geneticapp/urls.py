from django.urls import path, include
from rest_framework.routers import DefaultRouter
from geneticapp.views import CustomUserViewSet, AnalysisResultViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'analysis-results', AnalysisResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('dj_rest_auth.urls')),
    path('login/', views.obtain_auth_token),
    path('login/', include('dj_rest_auth.urls')),
]