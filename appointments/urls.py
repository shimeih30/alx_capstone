from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('', views.AppointmentListCreateView.as_view(), name='appointments-list'),
    path('<int:pk>/', views.AppointmentDetailView.as_view(), name='appointment-detail'),
    path('<int:pk>/cancel/', views.cancel_appointment, name='cancel-appointment'),
    path('provider/', views.provider_appointments, name='provider-appointments'),
    path('<int:appointment_id>/review/', views.AppointmentReviewCreateView.as_view(), name='appointment-review'),
]