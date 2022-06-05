import phonenumbers
import opencage
number=input("Enter your PhoneNumber With Country Code:")

from phonenumbers import geocoder
pepnumber=phonenumbers.parse(number)
location=geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier
service_number=phonenumbers.parse(number)
service_name=carrier.name_for_number(service_number,"en")
print(service_name)

from opencage.geocoder import OpenCageGeocode
key='Your API key'
geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
#print(results)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)

