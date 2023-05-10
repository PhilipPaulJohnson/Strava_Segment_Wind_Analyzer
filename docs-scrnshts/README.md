# Strava_Segment_Wind_Analyzer

OVERVIEW: This application will allow a cyclist publicly tracked by Strava to select any Strava segment effort for analysis/determination of optimal wind speed & direction of that segment

HOW IT WORKS: Using the Strava and Timeline Weather API, the application administrator will be able to view and select an athlete’s Strava segment(s) for analysis and insertion into the SQL database. When the database is sufficiently populated, the admin may use PG Admin to query the SQL database using new or preset scripts. The data may also be further analyzed within the app using new or previously imported Python data analysis modules or scripts. The main code can be found in segment_analyzer/drivercode.py

WHERE IT'S GOING: This app was developed to mainly showcase the simultaneous use of the technologies (listed below). While over-engineered for it's stated purpose, I wanted to generate a portfolio project in Flask using more complex connectivity. The app can be improved by packaging for easy install and the Python code improved with catch-alls, procedures wrapped into functions, OOP... in the next version


TECHNOLOGIES:

Python: base app / Psycopg database adapter 

Flask: framework

SQL Alchemy: tables & insertions prepared in Object Relational Model format

Alembic: database migrations will allow for rollbacks

Docker: Postgres server & database containerization

PG Admin: Postgres database administration & development


INSTALL:

1. insert flask/segment_analyzer folder (with files) into directory

2. create the flask folder venv / select venv interperter  

3. install requirements (python -m pip install -r requirements.txt)

4. create pgadmin containers with docker-compose.yml (docker compose up -d)

5. create server in PG Admin

6. (docker exec -i pg_container psql -c 'CREATE DATABASE efforts;')

7. check: __init__.py = (SQLALCHEMY_DATABASE_URI='postgresql://postgres@localhost:5432/efforts',) OR your db.uri

8. inside segment_analyzer folder: (flask db migrate) THEN (flask db upgrade)


AUTHORIZATION:

1. follow instructions to obtain Strava API authorization and subsequent authorization code. developers.strava.com/docs/getting-started/ 

2. insert authorization code into the nu_auth.py variable auth_code = '' and run. copy refresh and access tokens into the refresh_token & access_token variables (lines 42 & 44)

3. insert Strava API variables into drivercode.py (segment_id, start_date, end_date, per_page)

4. follow instructions to obtain Timeline Weather API authorization @ visualcrossing.com

5. insert Timeline Weather API variables into drivercode.py (apikey, maxDistance, timelineAuthCode)


RUN:

1. run drivercode.py