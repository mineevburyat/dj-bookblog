# sudo su postgree
# psql
CREATE USER blog WITH PASSWORD '34652817';
CREATE DATABASE blog OWNER blog ENCODING 'UTF8';
GRANT ALL PRIVILEGES ON DATABASE "blog" to blog;
# \du
# \l
# DROP DATABASE ddv;
# DROP USER sxc;