# script to analyze concerts.csv


from geopy.geocoders import Nominatim

loc = Nominatim(user_agent="GetLoc")

getLoc = loc.geocode("Viveiro")

print(getLoc.address)

print(f'Latitude = {getLoc.Latitude}')
print(f'Longitude = {getLoc.longitude}')

# read in concerts.csv


# iterate through and find the venue + find a way to convert to long/lat