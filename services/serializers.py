from rest_framework import serializers
from .models import ServiceCategory, Service, BusinessHours

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    provider_name = serializers.CharField(source='provider.business_name', read_only=True)
    
    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class BusinessHoursSerializer(serializers.ModelSerializer):
    day_name = serializers.CharField(source='get_day_of_week_display', read_only=True)
    
    class Meta:
        model = BusinessHours
        fields = '__all__'