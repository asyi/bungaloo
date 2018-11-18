# Bungaloo
Bungaloo is home rental API. Use it to create and manage a listing of homes for rent.

## What can it do?
1. Create a home listing: <http://localhost:8000/homes/create>
1. Retrieve a list of all home listings: <http://localhost:8000/homes/>
1. Retrieve a home listing: <http://localhost:8000/homes/ID>
1. Update a home listing: <http://localhost:8000/homes/ID>
1. Delete a home listing: <http://localhost:8000/homes/ID>
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

### Posting data
Bungaloo accepts the following fields:
```
    area_unit = string
    bathrooms = string
    bedrooms = integer
    home_size = integer
    home_type = string
    last_sold_date = date (yyyy-mm-dd)
    last_sold_price = integer
    link = url
    price = string
    property_size = integer
    rent_price = string
    rentzestimate_amount = integer
    rentzestimate_last_updated = date (yyyy-mm-dd)
    tax_value = float
    tax_year = integer
    year_built = integer
    zestimate_amount = integer
    zestimate_last_updated = date (yyyy-mm-dd)
    zillow_id = integer
    address = string
    city = string
    state = string
    zipcode = integer
```
You can send a post request to `http://localhost:8000/homes/create` with the following body:
```
{
    "area_unit": "",
    "bathrooms": "",
    "bedrooms": null,
    "home_size": null,
    "last_sold_date": null,
    "last_sold_price": null,
    "link": "",
    "price": "",
    "property_size": null,
    "rent_price": "",
    "rentzestimate_amount": null,
    "rentzestimate_last_updated": null,
    "tax_value": null,
    "tax_year": null,
    "year_built": null,
    "zestimate_amount": null,
    "zestimate_last_updated": null,
    "zillow_id": null,
    "address": "",
    "city": "",
    "state": "",
    "zipcode": null
}
```