from django.contrib import admin
from .models import Appointment, AppointmentReview

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'appointment_date', 'appointment_time', 'status', 'created_at')
    list_filter = ('status', 'appointment_date', 'created_at')
    search_fields = ('client__username', 'service__name', 'service__provider__business_name')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Appointment Details', {
            'fields': ('client', 'service', 'appointment_date', 'appointment_time')
        }),
        ('Status & Notes', {
            'fields': ('status', 'notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing existing appointment
            return self.readonly_fields + ('client', 'service')
        return self.readonly_fields

@admin.register(AppointmentReview)
class AppointmentReviewAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('appointment__client__username', 'appointment__service__name', 'comment')
    readonly_fields = ('created_at',)