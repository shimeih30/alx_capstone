from rest_framework import generics, filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import ServiceCategory, Service, BusinessHours
from .serializers import ServiceCategorySerializer, ServiceSerializer, BusinessHoursSerializer

class ServiceCategoryListView(generics.ListAPIView):
    """List all service categories"""
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    permission_classes = [AllowAny]

class ServiceListCreateView(generics.ListCreateAPIView):
    """List all active services or create a new one"""
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'provider']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'duration', 'created_at']
    ordering = ['name']

class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Get, update, or delete a specific service"""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class BusinessHoursListView(generics.ListAPIView):
    """Get business hours for a specific provider"""
    serializer_class = BusinessHoursSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        provider_id = self.kwargs.get('provider_id')
        return BusinessHours.objects.filter(provider_id=provider_id)