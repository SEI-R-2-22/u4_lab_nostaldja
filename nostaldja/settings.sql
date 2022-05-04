-- settings.sql

CREATE DATABASE nostaldja_sub;
CREATE USER subuser WITH PASSWORD '1234';
GRANT ALL PRIVILEGES ON DATABASE nostaldja_sub TO subuser;
