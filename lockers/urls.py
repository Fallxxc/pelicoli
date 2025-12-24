# from django.urls import path
from . import views

# urlpatterns = [
#     # Lockers
#     path('lockers/', views.LockerViewSet.as_view({'get': 'list', 'post': 'create'}), name='locker-list-create'),
#     path('lockers/<int:pk>/', views.LockerViewSet.as_view({
#         'get': 'retrieve',
#         'put': 'update',
#         'patch': 'partial_update',
#         'delete': 'destroy'
#     }), name='locker-detail'),

#     # Locations
#     # path('locations/', views.LocationViewSet.as_view({'get': 'list'}), name='location-list'),
#     path('locations/<int:pk>/', views.LocationViewSet.as_view({'get': 'retrieve'}), name='location-detail'),    
#     path('locations/', views.LocationViewSet.as_view({'get': 'list'}), name='location-list'),
#     # Auth API JWT (si tu utilises Django REST Framework SimpleJWT)
# ]
# # ath('lockers/', LockerViewSet.as_view({'get': 'list', 'post': 'create'}), name='locker-list-create'),
# #     path('lockers/<int:pk>/', LockerViewSet.as_view({
# #         'get': 'retrieve',
# #         'put': 'update',
# #         'patch': 'partial_update',
# #         'delete': 'destroy'
# #     }), name='locker-detail'),
    
# #     path('locations/', LocationViewSet.as_view({'get': 'list'}), name='location-list'),
# #     path('locations/<int:pk>/', LocationViewSet.as_view({'get': 'retrieve'}), name='location-detail'),


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router pour les API ViewSets
router = DefaultRouter()
router.register(r'locations', views.LocationViewSet)
router.register(r'lockers', views.LockerViewSet)

# Définir le namespace de l'application
app_name = 'lockers'

urlpatterns = [
    # Pages frontend (templates HTML)
    path('profile/', views.profile_view, name='profile'),
    path('index/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('lockers/', views.lockers_page, name='lockers'),
    path('locations/', views.locations_page, name='locations'),
    path('analytics/', views.analytics_page, name='analytics'),
    path('auth/login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('auth/refresh/', views.CustomTokenRefreshView.as_view(), name='token_refresh'),

]