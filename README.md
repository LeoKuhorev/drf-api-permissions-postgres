# Lab: 32, 33 - Permissions & Postgresql, Authentication & Production Server

## GETTING STARTED:

-   `poetry shell` to start your virtual environment
-   `poetry install` to install dependencies
-   create .env file with listed <a href="#env">below</a> variables and save it into 'server' directory
-   `docker-compose up --build` - to start docker container

In another terminal run:
-   `docker-compose exec web python manage.py makemigrations` - to generate DB schema
-   `docker-compose exec web python manage.py migrate` - to create DB schema
-   `docker-compose exec web python manage.py createsuperuser` - to create user with admin access

- `docker-compose exec web python manage.py test` - to run tests

If you're having troubles with installing `psycopg2` try this solution (for Mac users):
- `brew install openssl`
- `export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl/lib/`
- `pip3 install psycopg2`

### <a name="env"></a> ENV variables:

- `SECRET_KEY`=secret key for the app (typically 50-characters long string)
- `DEBUG`=should be set to True in development
- `ALLOWED_HOSTS`=localhost,127.0.0.1 (for testing)
- `DB_NAME`=PG database name
- `DB_USER`=PG database username
- `DB_PASS`=PG database password


## API:

`/` - landing page;

`user/register/` - register page, handles user registration;

`user/login/` - login page, allows a user to log in;

`user/profile/` - profile page, allows a user to view and edit their profile information (login required);

`user/logout/` - logout page, is shown when a user it logged out (login required);

`admin/` - site admin page;

`api/v1/` - API item list view;

`api/v1/<int:pk>` - API item detail view;

`api/token/` - Obtaining authorization tokens (requires  valid login and password);

`api/token/refresh/` - Refreshing access token by providing a valid refresh token;


### Dependency Documentation:

[Python (v. 3.8)](https://docs.python.org/3.8/)


[Django (v. 3.1.1)](https://docs.djangoproject.com/en/3.1/)

[Django REST Framework(v. 3.11.1)](https://www.django-rest-framework.org/)

[Django Crispy Forms (v. 1.9.2)](https://pypi.org/project/django-crispy-forms/)

[Django Environ (v. 0.4.5)](https://pypi.org/project/django-environ/)

### Dev Dependencies:

[Pylint-Django (v. 2.3.0)](https://pypi.org/project/pylint-django/)


[Link to PR](https://github.com/LeoKuhorev/drf-api-permissions-postgres/pull/1)
