### Fans Sports Club Mobile app backend 

#### Virtual environment/dependencies setup
- Create a virtaulenv
```
$ virtualenv -p python3 venv
$ source venv/bin/activate
```
- Install the dependencies
```
$ pip install -r requirements.txt
```

#### Postgresql setup:
- Install postgresql for database (ubuntu) 
```
$ sudo apt-get install postgresql postgresql-contrib
$ service postgresql start
$ sudo su postgres
$ psql
$ \l
$ CREATE DATABASE mydatabase_phase1;
```

#### Django setup:

- Setup the migrations
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
- Filling the database with data
```
$ ./load_datappytho
```
