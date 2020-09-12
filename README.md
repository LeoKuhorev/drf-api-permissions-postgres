# Lab: 32 - Permissions & Postgresql

## GETTING STARTED:

-   `poetry shell` to start your virtual environment
-   `poetry install` to install dependencies
-   create .env file with listed <a href="#env">below</a> variables and save it into 'server' directory
-   `docker-compose up --build` - to start docker container
-   `docker ps` to get your container ID (the one that has db in it)
-   `docker exec -it <container_id> psql -U postgres` to get into PSQL
-   run these commands in the psql shell to init the DB:
    `CREATE USER <username> WITH PASSWORD '<password>';`
    `ALTER ROLE <username> WITH superuser;`
    `CREATE DATABASE <db_name> OWNER <username>;`
-   `docker-compose exec web python manage.py makemigrations` - to generate DB schema
-   `docker-compose exec web python manage.py migrate` - to create DB schema
-   `docker-compose exec web python manage.py createsuperuser` - to create user with admin access

If you're having troubles with installing `psycopg2` try this solution (for Mac users):
`brew install openssl`
`export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl/lib/`
`pip3 install psycopg2`

### <a name="env"></a> ENV variables:

`SECRET_KEY`=secret key for the app (typically 50-characters long string)
`DEBUG`=should be set to True in development
`ALLOWED_HOSTS`=localhost,127.0.0.1 (for testing)
`DB_NAME`=PG database name
`DB_USER`=PG database username
`DB_PASS`=PG database password
