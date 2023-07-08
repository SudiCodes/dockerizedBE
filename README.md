# dockerized Backend

Environment:

1. Python:
   Python 3.10.6
2. OS:
   PRETTY_NAME="Ubuntu 22.04.2 LTS"
   NAME="Ubuntu"
   VERSION_ID="22.04"
   VERSION="22.04.2 LTS (Jammy Jellyfish)"
   VERSION_CODENAME=jammy
   ID=ubuntu
   ID_LIKE=debian
3. Django:
   Django 4.1.4
   Project Name: backend
4. Postgres:
   version = psql (PostgreSQL) 15.2 (Ubuntu 15.2-1.pgdg22.04+1)

Getting Started:

1. install prerequisite for creating venv:
   - apt install python3.10-venv
2. Create virtual env:
   - python3 -m venv venv
   - source venv/bin/activate
3. Installing Djnago
   - pip install Django
4. Installing requirements
   - pip3 install -r requirements.txt
5. Installing Postgres SQL
   - bash scripts:
     - sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
     - wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
     - sudo apt-get update
     - sudo apt-get -y install postgresql
   - verify installation:
     - psql --version ("psql (PostgreSQL) 15.2 (Ubuntu 15.2-1.pgdg22.04+1)")
     - sudo -u postgres psql (move to psql terminal)
     - \password postgres (create password for default user)

Django commands:

1. django-admin startproject <PROJECT_NAME>
2. python3 manage.py createapp <APP_NAME>
3. python3 manage.py makemigrations
4. python3 manage.py migrate
5. python3 manage.py createsuperuser
6. python3 manage.py runserver (<IP:PORT>\*Optional)

RUN backend with SSL:
`gunicorn --certfile=certs/server.crt --keyfile=certs/server.key mt_backend.wsgi:application`
