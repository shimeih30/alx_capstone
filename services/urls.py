from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('categories/', views.ServiceCategoryListView.as_view(), name='categories'),
    path('', views.ServiceListCreateView.as_view(), name='services-list'),
    path('<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
    path('business-hours/<int:provider_id>/', views.BusinessHoursListView.as_view(), name='business-hours'),
]