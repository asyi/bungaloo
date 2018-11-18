# Bungaloo
Bungaloo is home rental API. Use it to create and manage a listing of homes for rent.

## What can it do?
1. Create a home listing: <http://127.0.0.1:8000/homes/create>
1. Retrieve a list of all home listings: <http://127.0.0.1:8000/homes/>
1. Retrieve a home listing: <http://127.0.0.1:8000/homes/ID>
1. Update a home listing: <http://127.0.0.1:8000/homes/ID>
1. Delete a home listing: <http://127.0.0.1:8000/homes/ID>
1. Import home data from a CSV file

### Environment
1. Bungaloo is built with Python3
1. It also uses Pipenv: <https://pipenv.readthedocs.io/en/latest/>

### Installation guide
1. `git clone git@github.com:asyi/bungaloo.git`
1. `cd bungaloo/`
1. `pipenv install django==2.1.3`
1. `pipenv install djangorestframework`

### How to run migrations
1. `pipenv shell`
1. `cd bungaloo/`
1. `python manage.py makemigrations`
1. `python manage.py migrate`

### How to run server
1. `pipenv shell`
1. `cd bungaloo/`
1. `python manage.py runserver`

### How to import CSV data
Bungaloo has a csv file called 'challenge_data.csv', which contains home data. To import the data to Bungaloo's database, do the following:
1. `pipenv shell`
1. `cd bungaloo/`
1. `python manage.py loadcsv --csvfile challenge_data.csv`

### How to query data from CLI
1. `pipenv shell`
1. `cd bungaloo/`
1. `python manage.py shell`
1. `from api.models import Home`
1. Example query to blow the database: `Home.objects.all().delete()`

### How to run tests
Bungaloo currently has no tests. However, if it were to have test, you can run them by doing the following:
1. `pipenv shell`
1. `cd bungaloo/`
1. `python manage.py test`
