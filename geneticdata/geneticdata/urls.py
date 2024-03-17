# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from geneticapp.views import CustomUserViewSet, AnalysisResultViewSet
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from geneticapp.views import user_login

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'analysis-results', AnalysisResultViewSet)

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include(router.urls)),
    path('login/', user_login, name='login'),
    path('api-auth/', include('rest_framework.urls')),  
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]




