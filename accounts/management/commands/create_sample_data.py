from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from accounts.models import ServiceProvider
from services.models import ServiceCategory, Service, BusinessHours
from appointments.models import Appointment
from datetime import time, date

User = get_user_model()

class Command(BaseCommand):
    help = 'Create sample data for testing'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')

        # Create service categories
        categories = [
            {'name': 'Healthcare', 'description': 'Medical and health services'},
            {'name': 'Beauty', 'description': 'Beauty and wellness services'},
            {'name': 'Fitness', 'description': 'Fitness and sports services'},
            {'name': 'Education', 'description': 'Educational and tutoring services'},
        ]

        for cat_data in categories:
            category, created = ServiceCategory.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Create sample users
        if not User.objects.filter(username='provider1').exists():
            provider_user = User.objects.create_user(
                username='provider1',
                email='provider@example.com',
                password='testpass123',
                first_name='Dr. Sarah',
                last_name='Johnson',
                user_type='provider'
            )
            self.stdout.write('Created provider user')

            # Create service provider profile
            provider = ServiceProvider.objects.create(
                user=provider_user,
                business_name='HealthCare Plus',
                description='Comprehensive healthcare services',
                address='123 Main Street',
                city='New York',
                state='NY',
                zip_code='10001',
                is_verified=True
            )
            self.stdout.write('Created service provider profile')

            # Create business hours
            for day in range(5):  # Monday to Friday
                BusinessHours.objects.create(
                    provider=provider,
                    day_of_week=day,
                    opening_time=time(9, 0),
                    closing_time=time(17, 0)
                )

            # Create sample services
            healthcare_cat = ServiceCategory.objects.get(name='Healthcare')
            services_data = [
                {'name': 'General Consultation', 'duration': 30, 'price': 100.00},
                {'name': 'Physical Therapy', 'duration': 60, 'price': 80.00},
                {'name': 'Health Checkup', 'duration': 45, 'price': 150.00},
            ]

            for service_data in services_data:
                Service.objects.create(
                    provider=provider,
                    category=healthcare_cat,
                    name=service_data['name'],
                    description=f"Professional {service_data['name'].lower()}",
                    duration=service_data['duration'],
                    price=service_data['price']
                )
                self.stdout.write(f'Created service: {service_data["name"]}')

        # Create sample client
        if not User.objects.filter(username='client1').exists():
            User.objects.create_user(
                username='client1',
                email='client@example.com',
                password='testpass123',
                first_name='John',
                last_name='Doe',
                user_type='client'
            )
            self.stdout.write('Created client user')

        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data!')
        )
        self.stdout.write('Login credentials:')
        self.stdout.write('Provider: provider1 / testpass123')
        self.stdout.write('Client: client1 / testpass123')