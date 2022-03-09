#-*-coding:utf8;-*-
#qpy:console

# importing modules

from geopy.geocoders import Nominatim 
location = input("Enter location in form latitude, longitude:\n")
# calling the nominatim tool
geoLoc = Nominatim(user_agent="GetLoc") 
# passing the coordinates

try:
    locname = geoLoc.reverse(location) 
    # printing the address/location name
    try:
        print(locname.address)
    except AttributeError:
        print('No land address!')
except ValueError:
    print('ERROR!: Coordinates are not fully numeric!')

    
