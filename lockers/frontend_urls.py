from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('lockers/', views.lockers_page, name='lockers-page'),
    path('locations/', views.locations_page, name='locations-page'),
    path('analytics/', views.analytics_page, name='analytics-page'),
]
