import requests

path_url = 'http://api.postcodes.io/postcodes/'
arguements = 'mk88dt'

post_codes = requests.get(path_url+arguements)

dict_response = post_codes.json()

# 1- Play around with API and getting data
# This prints out the keys in the get request
print(dict_response.keys())
#This prints out the status of the website (which inlcudes the URL and argument passed through)
print(dict_response['status'])
#This prints out the results as a dictionary
print(dict_response['result'])

# 2 - prints out the longitude, latitude, nuts and admin_ward of a postcode
print('longitude: ' + dict_response['result']['longitude'])
print('latitude: ' + dict_response['result']['latitude'])
print('nuts: ' + dict_response['result']['nuts'])
print('admin_ward' + dict_response['result']['admin_ward'])

# 3 - function that returns the latitude of a postcode
def postcode_latitude():
    user_postcode = input('Input: ')
    path_url = 'http://api.postcodes.io/postcodes/'
    result = requests.get(path_url + user_postcode.strip())
    post_code_dict = result.json()
    return post_code_dict['result']['latitude']

# 4 - function that returns the longitude of a postcode
def postcode_longitude():
    user_postcode = input('Input: ')
    path_url = 'http://api.postcodes.io/postcodes/'
    result = requests.get(path_url + user_postcode.strip())
    post_code_dict = result.json()
    return post_code_dict['result']['longitude']