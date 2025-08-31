from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('providers/', views.ServiceProviderListCreateView.as_view(), name='providers-list'),
    path('providers/<int:pk>/', views.ServiceProviderDetailView.as_view(), name='provider-detail'),
]