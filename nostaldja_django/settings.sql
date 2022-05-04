-- settings.sql
CREATE DATABASE nostaldja;
CREATE USER nostaldjauser WITH PASSWORD 'user';
GRANT ALL PRIVILEGES ON DATABASE nostaldja TO nostaldjauser;