-- settings.sql
CREATE DATABASE nostaldja;
CREATE USER nostaldja_user WITH PASSWORD 'nostaldja';
GRANT ALL PRIVILEGES ON DATABASE tunr TO nostaldja_user;