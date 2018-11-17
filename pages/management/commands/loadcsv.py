import csv

from django.core.management.base import BaseCommand
from pages.models import Home

class Command(BaseCommand):
    help = 'Loads CSV data: homes'

    def add_arguments(self, parser):
        parser.add_argument('--csvfile', nargs='+', type=str)
    
    def handle(self, *args, **options):

        def format_date(date):
            if date !='':
                print(f'date: {date}')
                month = date.split('/')[0]
                day = date.split('/')[1]
                year = date.split('/')[2]
                return '%s-%s-%s' % (year, month, day)

        for f in options['csvfile']:
            with open(f) as csvfile:
                reader = csv.reader(csvfile)
                line_count = 0
                next(reader, None)
                for row in reader:
                    line_count += 1

                    print(f'On row: {line_count}')
                    print(f'This home has the following properties: {", ".join(row)}')

                    area_unit = row[0]
                    bathrooms = row[1]
                    bedrooms = row[2] or 0
                    home_size = row[3] or 0
                    home_type = row[4]
                    last_sold_date = format_date(row[5])
                    last_sold_price = row[6] or 0
                    link = row[7] or 0
                    price = row[8]
                    property_size = row[9] or 0
                    rent_price = row[10]
                    rentzestimate_amount = row[11] or 0
                    rentzestimate_last_updated = format_date(row[12])
                    tax_value = row[13] or 0
                    tax_year = row[14] or 0
                    year_built = row[15] or 0
                    zestimate_amount = row[16] or 0
                    zestimate_last_updated = format_date(row[17])
                    zillow_id = row[18] or 0
                    address = row[19]
                    city = row[20]
                    state = row[21]
                    zipcode = row[22] or 0

                    new_home = Home(
                        area_unit=area_unit,
                        bathrooms=bathrooms,
                        bedrooms=bedrooms,
                        home_size=home_size,
                        last_sold_date=last_sold_date,
                        last_sold_price=last_sold_price,
                        link=link,
                        price=price,
                        property_size=property_size,
                        rent_price=rent_price,
                        rentzestimate_amount=rentzestimate_amount,
                        rentzestimate_last_updated=rentzestimate_last_updated,
                        tax_value=tax_value,
                        tax_year=tax_year,
                        year_built=year_built,
                        zestimate_amount=zestimate_amount,
                        zestimate_last_updated=zestimate_last_updated,
                        zillow_id=zillow_id,
                        address=address,
                        city=city,
                        state=state,
                        zipcode=zipcode)
                    new_home.save()

                    self.stdout.write(self.style.SUCCESS('Successfully saved home'))
                    