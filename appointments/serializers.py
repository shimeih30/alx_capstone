from rest_framework import serializers
from django.utils import timezone
from datetime import datetime
from .models import Appointment, AppointmentReview
from services.serializers import ServiceSerializer
from accounts.serializers import UserSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    service_details = ServiceSerializer(source='service', read_only=True)
    client_details = UserSerializer(source='client', read_only=True)
    provider_name = serializers.CharField(source='service.provider.business_name', read_only=True)
    
    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ['client', 'created_at', 'updated_at']

    def validate(self, data):
        # Combine date and time for validation
        appointment_datetime = datetime.combine(
            data['appointment_date'], 
            data['appointment_time']
        )
        
        # Convert to timezone-aware datetime
        if timezone.is_naive(appointment_datetime):
            appointment_datetime = timezone.make_aware(appointment_datetime)
        
        # Check if appointment is in the past
        if appointment_datetime <= timezone.now():
            raise serializers.ValidationError("Cannot book appointments in the past")
        
        # Check if slot is already taken (excluding current instance for updates)
        existing_appointment = Appointment.objects.filter(
            service=data['service'],
            appointment_date=data['appointment_date'],
            appointment_time=data['appointment_time'],
            status__in=['pending', 'confirmed']
        )
        
        # Exclude current instance if updating
        if self.instance:
            existing_appointment = existing_appointment.exclude(pk=self.instance.pk)
            
        if existing_appointment.exists():
            raise serializers.ValidationError("This time slot is already booked")
        
        return data

class AppointmentReviewSerializer(serializers.ModelSerializer):
    appointment_details = AppointmentSerializer(source='appointment', read_only=True)
    
    class Meta:
        model = AppointmentReview
        fields = '__all__'
        read_only_fields = ['created_at']