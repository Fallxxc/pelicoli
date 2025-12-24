# from django.contrib import admin
# from django.urls import path, include
from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     # Authentification (login/logout)
#     path('login/', auth_views.LoginView.as_view(template_name='lockers/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),

#     # Frontend (pages HTML)
#     path('', include('lockers.frontend_urls')),

#     # API REST
#     path('api/', include('lockers.urls')),
# ]
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from lockers import views
from lockers.views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

# Router pour les API
router = DefaultRouter()
router.register(r'locations', views.LocationViewSet)
router.register(r'lockers', views.LockerViewSet)

urlpatterns = [
    # Admin Django
    path('admin/', admin.site.urls),
    
    # API REST
    path('api/', include(router.urls)),
    
    # Authentification JWT
    path('api/auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', auth_views.LoginView.as_view(template_name='lockers/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Pages frontend (avec namespace 'lockers')
    path('', include('lockers.urls', namespace='lockers')),
]