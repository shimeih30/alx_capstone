from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Appointment, AppointmentReview
from .serializers import AppointmentSerializer, AppointmentReviewSerializer

class AppointmentListCreateView(generics.ListCreateAPIView):
    """List user's appointments or create a new one"""
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Appointment.objects.filter(client=self.request.user)

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Get, update, or delete a specific appointment"""
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Appointment.objects.filter(client=self.request.user)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cancel_appointment(request, pk):
    """Cancel an appointment"""
    appointment = get_object_or_404(Appointment, pk=pk, client=request.user)
    
    if appointment.status in ['completed', 'cancelled']:
        return Response(
            {'error': 'Cannot cancel a completed or already cancelled appointment'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    appointment.status = 'cancelled'
    appointment.save()
    
    return Response({'message': 'Appointment cancelled successfully'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def provider_appointments(request):
    """Get appointments for service provider"""
    try:
        provider = request.user.provider_profile
        appointments = Appointment.objects.filter(service__provider=provider)
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response(
            {'error': 'User is not a service provider'}, 
            status=status.HTTP_403_FORBIDDEN
        )

class AppointmentReviewCreateView(generics.CreateAPIView):
    """Create a review for a completed appointment"""
    serializer_class = AppointmentReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        appointment = get_object_or_404(
            Appointment, 
            pk=self.kwargs['appointment_id'], 
            client=self.request.user,
            status='completed'
        )
        serializer.save(appointment=appointment)