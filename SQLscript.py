import postgresql

db = postgresql.open('pq://postgres:postgres@localhost:5432/limb')
db.execute("CREATE USER admin WITH LOGIN SUPERUSER INHERIT CREATEDB CREATEROLE "
"REPLICATION;GRANT postgres TO admin;CREATE DATABASE limb WITH OWNER = postgres ENCODING = 'UTF8'"
"LC_COLLATE = 'Russian_Russia.1251' LC_CTYPE = 'Russian_Russia.1251' "
"TABLESPACE = pg_default CONNECTION LIMIT = -1;")
