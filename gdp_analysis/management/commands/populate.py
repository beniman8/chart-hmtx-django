import itertools
from django.core.management.base import BaseCommand
from gdp_analysis.models import GDP
from django.conf import settings
import json


class Command(BaseCommand):
    help = 'Load Courses and Modules'

    def handle(self, *args, **kwargs):
        if not GDP.objects.count():
            datafile = settings.BASE_DIR / 'data' / 'data.json'
            with open(datafile,'r') as f:
                data = json.load(f)


            data = itertools.dropwhile(lambda x: x['Country Name'] != 'Afghanistan',data)


            gdps = [] 
            for d in data:
                gdps.append(GDP(
                    
                    country=d['Country Name'],
                    country_code=d['Country Code'],
                    year=d['Year'],
                    gdp=d['Value'],
                              
                    ))

            print(gdps)
            GDP.objects.bulk_create(gdps)
        