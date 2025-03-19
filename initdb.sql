# sudo su postgree
# psql
CREATE USER bloguser WITH PASSWORD '34652817';
CREATE DATABASE blogdb OWNER bloguser ENCODING 'UTF8';
GRANT ALL PRIVILEGES ON DATABASE "blogdb" to bloguser;
# \du
# \l
# DROP DATABASE ddv;
# DROP USER sxc;