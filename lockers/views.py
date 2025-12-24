from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Location, Locker
from .serializers import LocationSerializer, LockerSerializer
from .permissions import IsAdminOrOperator

# ---------------------------
# Vues API (existantes)
# ---------------------------
class LocationViewSet(ReadOnlyModelViewSet):
    """
    Liste des emplacements (Auchan, stations, gares)
    Affichés sur la carte (lecture seule)
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class LockerViewSet(ModelViewSet):
    """
    CRUD des lockers PELICOLIS
    Réservé aux ADMIN & OPERATOR
    """
    queryset = Locker.objects.all()
    serializer_class = LockerSerializer
    permission_classes = [IsAdminOrOperator]

# ---------------------------
# Vues frontend (templates HTML)
# ---------------------------
@login_required
def dashboard(request):
    return render(request, 'lockers/dashboard.html')

@login_required
def lockers_page(request):
    return render(request, 'lockers/lockers.html')

@login_required
def locations_page(request):
    return render(request, 'lockers/locations.html')

@login_required
def analytics_page(request):
    return render(request, 'lockers/analytics.html')

# Vue pour la carte (page d'accueil)
def index(request):
    return render(request, 'lockers/index.html')

def login(request):
    return render(request, 'lockers/login.html')
# ---------------------------
# Authentification JWT personnalisée
# ---------------------------
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Ajouter des informations personnalisées dans le token
        token['username'] = user.username
        token['email'] = user.email
        token['role'] = "ADMIN" if user.is_staff else "VIEWER"
        
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
    
def profile_view(request):
    return render(request, "lockers/profil.html")
    