from googleplaces import GooglePlaces, types, lang
APIKEY = 'YOUR_API_KEY'
google_places = GooglePlaces(APIKEY)

def FetchPoi():

    cordiates = "22.260745,39.796600"   
    mosque = ['school','education','studies','principle','knowledge']

    for category in mosque:
        query_result = google_places.nearby_search(location="Karachi", keyword=category,radius=50000, types=[types.TYPE_SCHOOL], language=lang.ENGLISH_GREAT_BRITAIN)
        for place in query_result.places:
            print(place.name,place.geo_location)
