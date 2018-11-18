# Bungaloo
Bungaloo is home rental API. Use it to create and manage a listing of homes for rent.

## What can it do?
1. Create a home listing: <http://127.0.0.1:8000/homes/create>
1. Retrieve a list of all home listings: <http://127.0.0.1:8000/homes/>
1. Retrieve a home listing: <http://127.0.0.1:8000/homes/ID>
1. Update a home listing: <http://127.0.0.1:8000/homes/ID>
1. Delete a home listing: <http://127.0.0.1:8000/homes/ID>
1. Import home data from a CSV file

### How to import CSV data
Bungaloo has a csv file called 'challenge_data.csv', which contains home data. To import the data to Bungaloo's database, do the following:
1. `pipenv shell`
2. `cd bungaloo/`
3. `python manage.py loadcsv --csvfile challenge_data.csv`

### How to run tests
Bungaloo currently has no tests. However, if it were to have test, you can run them by doing the following:
1. `pipenv shell`
2. `cd bungaloo/`
3. `python manage.py test`

### How to run server
1. `pipenv shell`
2. `cd bungaloo/`
3. `python manage.py runserver`
