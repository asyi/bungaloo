from django.db import models

class Home(models.Model):
    area_unit = models.CharField(blank=True, max_length=200)
    bathrooms = models.CharField(blank=True, max_length=200, default='')
    bedrooms = models.IntegerField(blank=True, null=True)
    home_size = models.IntegerField(blank=True, null=True)
    home_type = models.CharField(blank=True, max_length=200)
    last_sold_date = models.DateField(blank=True, null=True)
    last_sold_price = models.IntegerField(blank=True, null=True)
    link = models.URLField(blank=True)
    price = models.CharField(blank=True, max_length=200)
    property_size = models.IntegerField(blank=True, null=True)
    rent_price = models.CharField(blank=True, max_length=200)
    rentzestimate_amount = models.IntegerField(blank=True, null=True)
    rentzestimate_last_updated = models.DateField(blank=True, null=True)
    tax_value = models.FloatField(blank=True, null=True)
    tax_year = models.IntegerField(blank=True, null=True)
    year_built = models.IntegerField(blank=True, null=True)
    zestimate_amount = models.IntegerField(blank=True, null=True)
    zestimate_last_updated = models.DateField(blank=True, null=True)
    zillow_id = models.IntegerField(blank=True, null=True)
    address = models.CharField(blank=True, max_length=200)
    city = models.CharField(blank=True, max_length=200)
    state = models.CharField(blank=True, max_length=2)
    zipcode = models.IntegerField(blank=True, null=True)

    def __str__(self):
        """Return a human readable rep of the model instance"""
        return "{}".format(self)