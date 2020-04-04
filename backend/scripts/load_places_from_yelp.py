import django
import sys
import os
sys.path.append(os.path.dirname(__file__) + '/..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'carebackend.settings'
django.setup()
from places.models import Place, Area
import sys
from places import yelpAPI as yelp
import places_json_to_csv as jtc


def load_places_to_db(term = '', location = 'Seattle', offset = 0):
    print(f"Getting businesses from {location}, offest: {offset}")

    # Get buinesses from Yelp
    result = yelp.query_api(term, location, offset)

    # using django-admin loaddata
    bz = jtc.json_to_csv("businesses",result)

    for row in bz:
        #skip non-seattle businesses
        if row['area'] != 'Seattle':
            continue

        try:
            p = Place.objects.get(place_id=row['place_id'])
        except Place.DoesNotExist:
            p = Place(place_id=row['place_id'])  

        if not p.name:
            p.name = row['name']  
        p.lat = row['lat']
        p.lng = row['lng']
        p.user_rating = row['user_rating']
        p.num_ratings = row['num_ratings']
        p.address = row['address']
        p.place_url = row['place_url']
        p.place_types = row['place_types']
        p.save()

    print(f"Finished loading {len(bz)} of businesses to database")

if __name__ == "__main__":
    seattle_zipcodes = "98060, 98101, 98102, 98103, 98104, 98105, 98106, 98107, 98108, 98109, 98111, 98112, 98113, 98114, 98115, 98116, 98117, 98118, 98119, 98121, 98122, 98124, 98125, 98126, 98127, 98129, 98130, 98131, 98132, 98133, 98134, 98136, 98138, 98139, 98140, 98141, 98144, 98145, 98146, 98148, 98150, 98151, 98154, 98155, 98158, 98160, 98161, 98164, 98165, 98166, 98168, 98170, 98171, 98174, 98175, 98177, 98178, 98181, 98184, 98185, 98188, 98190, 98191, 98194, 98195, 98198, 98199"
    ziplist = seattle_zipcodes.split(', ') 
    
    for zipcode in ziplist:
        for offset in range (0,951,50):
            load_places_to_db(location = 'Seattle '+zipcode, offset = offset)