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



