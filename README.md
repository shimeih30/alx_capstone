Booking App Backend

This project is the backend for my booking application, built with Django and Django REST Framework. 
The idea is to create a reliable system that connects service providers (like hairdressers, nail techs, 
massage therapists,dentists and tutors etc.) with customers who want to book appointments. The backend handles user accounts, 
authentication, service listings, appointment scheduling, and reviews. Later on, I plan to add payments and notifications to make the 
platform more complete in the future.

I chose this project because I wanted to build something practical that could actually work in real life, especially in Zimbabwe
where most service bookings are still informal. A platform like this makes it easier for customers to find trusted providers 
while also helping providers manage their time and grow their businesses. 
At the same time, it gives me the chance to practice designing APIs, structuring a backend, and thinking about scalability.

On the technical side, the project uses JWT authentication for secure logins, and the API endpoints are structured following RESTful principles. The 
app is broken into modular Django apps: accounts (for users), services (for service provider listings), appointments (for booking and scheduling), 
and reviews (for ratings and feedback). For the database, I’m using SQLite in development since it’s simple and lightweight, but the plan is to run with 
PostgreSQL in production since it's more robust and scalable.

The environment is managed with pip3 and a requirements.txt file, migrations are handled through Django’s built-in ORM, and everything 
is version-controlled with Git and github. The goal is to keep the backend clean and extendable so it can plug into a React frontend or 
my mobile app that I am beginning to build soon.

To set this up yourself, just clone the repo, create a virtual environment, install the dependencies, run migrations, and start the dev server. From there, 
you can register an account, log in to get a token, create and browse services, book appointments, and leave reviews — all through the exposed API endpoints.

This project is my ALx Africa capstone project and also a personal milestone because I have had this app idea for years and ended up deciding to
enroll in this course to start working on the MVP and understand what I am doing before bringing experienced devs to the project. 
I didn’t want to just vibe-code this project, I wanted to actually understand what’s happening under the hood, 
from the models to the migrations to the way authentication flows work.

Here is the Documentation and Project Structure


API Features

 User Management
- Custom user model with client/provider types
- User registration and authentication
- Service provider profiles with business information
- User profiles with contact details

 Services Management
- Service categories (Healthcare, Beauty, Fitness, etc.)
- Service listings with pricing and duration
- Business hours management
- Search and filtering capabilities

 Appointments System
- Book appointments with conflict checking
- Multiple appointment statuses (pending, confirmed, completed, cancelled)
- Appointment management for both clients and providers
- Review system with ratings

 API Features
- RESTful API endpoints
- Django REST Framework integration
- Admin interface for data management
- CORS support for frontend integration

 Technology Stack

- Backend Framework: Django 4.2.7
- API Framework: Django REST Framework 3.14.0
- Database: SQLite (development) / PostgreSQL (production ready)
- Authentication: Django's built-in authentication
- Media Files: Pillow for image handling

Project Structure

```
appointments-booking-app/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── appointments_booking/          Responsible for  Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/                      Responsible for  User management
│   ├── models.py                 Responsible for  User and ServiceProvider models
│   ├── views.py                  Responsible for  Authentication views
│   ├── serializers.py            Responsible for  API serializers
│   └── admin.py                  Responsible for  Admin configuration
├── services/                      Responsible for  Services management
│   ├── models.py                 Responsible for  Service, Category, BusinessHours models
│   ├── views.py                  Responsible for  Service API views
│   ├── serializers.py            Responsible for  Service serializers
│   └── admin.py                  Responsible for  Admin configuration
└── appointments/                  Responsible for  Appointments system
├── models.py                 Responsible for  Appointment and Review models
├── views.py                  Responsible for  Appointment API views
├── serializers.py            Responsible for  Appointment serializers
└── admin.py                  Responsible for  Admin configuration



For Installation & Setup

Prerequisites
- Python 3.8+
- pip
- Git

 Local Development Setup

1. Clone the repository:
   ```bash command:
  	 git clone https://github.com/shimeih30/alx_capstone
   	cd appointments-booking-app
python3 -m venv venv 	(windows source venv/bin/activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
To access the API go to http://127.0.0.1:8000/api/ in ypur browser
For Admin go to: http://127.0.0.1:8000/admin/

```




Thank you for passing by and enjoy some ascii art down below


```
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%@@@@@@%%@@@@@@@%%%@@@@@@%%%%@%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%
%%%%%%%%%@@@-     .@@  @@@@.  @@@@@  @@@: =@+ @@@*%@@@%%%%%%%%%%%
%%%%%%%%%@@%@@  @: @@* +@@@ =  @@@@   @@  @% .-  @@@@@@%%%%%%%%%%
%%%%%%%%%%%@@@  @+ .    @@. -   @@@ =    %@   =@@@@@@@@%%%%%%%%%%
%%%%%%%%%%@@@@- =@  @@  %@ -*%@  %% @@  .@  %-  *@@@@@%%%%%%%%%%%
%%%%%%%%%@@@@@@  @* %@@+@@@@@@@@:*@:@@@@@@@@@@@.  @%%%%%%%%%%%%%%
%%%%%%%%%%%@@@@@@@@@@@@@-@@@@@@@@@@@-%@@@  @@@@@@@@%%%%%%%%%%%%%%
%%%%%%%%%%%@@@@@@. :@#@ .@@  @%  +@@  @@@  *@@@@@@@%%%%%%%%%%%%%%
%%%%%%%%%%%@@@@@@@@.    @@@ .@@@  =@  %@@  :@@@@@@%%%%%%%%%%%%%%%
%%%%%%%%%%%@@@@@@@@@@  @@@@   @@  %@@      @@@@@@@%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%@@@@@* %@@@#@@.  -@@@@@@@+@@@@%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@%@@@@@@@%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%:+====%%*%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*====@@@@@@%:%%%%%%
%%%%%%%%%%%-========::%%%%%%%%%%%%%%%%%%%%%%:====@@@@@@@@@=:%%%%%
%%%%%%%%%%==@@@@@@@=====-%%%%%%%%%%%%%%%%%%*===@@@@@@@@@@@%-%%%%%
%%%%%%%%%%*=@@@@@@@@@@====++%%%%%%%%%%%%%*====@@@@@@@@@@@@@:%%%%%
%%%%%%%%%%:=@@@@@@@@@@@@====+++::----+---========%@@@@@@@@@:%%%%%
%%%%%%%%%%+=@@@@@@@@@@@%======--=*---*=--=============%@@@%:%%%%%
%%%%%%%%%%%-@@@@@@@%===========:==---====================%%-%%%%%
%%%%%%%%%%%-%@@@@==================+=======================:%%%%%
%%%%%%%%%%%%-@@=============================================-%%%%
%%%%%%%%%%%%++===============================================:%%%
%%%%%%%%%%%%:======================%@@@@@@%==================:%%%
%%%%%%%%%%%%-================@@@@@@@@@@@@@@@@%+%%=============*%%
%%%%%%%%%%%*+=============@+*%@@@@@@@@@@@@@-=@@@@+@===========*%%
%%%%%%%%%%%*+===========%%@@@@**@@@@@@@@@@=@@@@@@@@@@========:=%%
%%%%%%%%%%%%-=========@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+:--*=-%%%
%%+::--:%%%%-========@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@====-%%%%
%%-@@@@@@:-%%-+*:---=@@@@@@@@@@@@@@@@:*@@@%@@@@@@@@@@@@@==::%%%%%
%=*@@@@@#@@::%-*====@@@@@@@@@@@@@=-:=%%%%-@@@@@@@@@@@@@=:-%%%%%%%
%++@@@@=@@@=*:%=-*==%@@@@@@@@@@@@@@+%%%%%-@@@@@@@@@@%:-=%%%%%%%%%
%%:=%@@@==@==:+%%%+-:=%#@@@@@@@@@@@@-%%+-@@@@@@@+--*%%%%%%%%%%%%%
%%:====@======-%%%%%%%::---*=@@@@@@@@%=*-----*%%%%%%%%%%%%%%%%%%%
%%%:==========++%%%%=:==================-%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%-=========-%%%=:==========+===*===*=%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%-========-%%-==========@::=+::=--%%%%%%%%%%%%%%%%%%%%%%%%%
----------.------.-.------------------.--------------------------


```



