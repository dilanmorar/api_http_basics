import requests

# build url
path_url = 'http://api.postcodes.io/postcodes/'
arguements = 'e146gt'

post_codes = requests.get(path_url+arguements)

print(post_codes)