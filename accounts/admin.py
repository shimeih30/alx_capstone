from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ServiceProvider

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_type', 'first_name', 'last_name', 'is_active')
    list_filter = ('user_type', 'is_active', 'is_staff', 'created_at')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('user_type', 'phone', 'date_of_birth')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('user_type', 'phone', 'date_of_birth')}),
    )

@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'user', 'city', 'state', 'is_verified', 'rating', 'created_at')
    list_filter = ('is_verified', 'city', 'state', 'created_at')
    search_fields = ('business_name', 'user__username', 'user__email', 'description')
    readonly_fields = ('rating', 'created_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'business_name', 'description')
        }),
        ('Location', {
            'fields': ('address', 'city', 'state', 'zip_code')
        }),
        ('Contact & Media', {
            'fields': ('website', 'profile_image')
        }),
        ('Status', {
            'fields': ('is_verified', 'rating')
        }),
    )