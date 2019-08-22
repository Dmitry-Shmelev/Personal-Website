# Personal Website


## Description

This is my personal website. I developed it with Django on backend and Bootstrap4 on frontend, Posgresql by database. You can change your projects in page by adding them to database at admin.


## Installation

You have to install virtualenv in your project directory and activate it.

```bash
$ python3 -m venv virtual/env
$ source virtual/env/bin/active
```

In your virtual environment, install django and all requirement libraries.

```bash
(env)$ pip3 install -r requirements.txt
```

Next, you have to install psycopg2 to use PostgreSQL.
```bash
(env)$ export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl/lib/
(env)$ pip3 install psycopg2
```

Create database and user by psql command.
```bash
(env)$ psql
(env)$ CREATE USER user_name WITH PASSWORD 'user_password';
(env)$ CREATE DATABASE database_name WITH OWNER user_name;
```

You can backup database from db.sqlite3 and restore to PostgreSQL.
```bash
(env)$ python3 manage.py dumpdata > datadump.json
(env)$ python3 manage.py loaddata datadump.json
```

Migrate your database.
```bash
(env)$ python3 manage.py makemigrations
(env)$ python3 manage.py migrate
```

Then run your server by this script.

```bash
(env)$ python3 manage.py runserver
```

You can see my website at https://localhost:8000.

Also go into admin panel at https://localhost:8000/admin


## License

[MIT](https://choosealicense.com/licenses/mit/)
