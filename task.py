import requests

path_url = 'http://api.postcodes.io/postcodes/'
arguements = 'e146gt'

post_codes = requests.get(path_url+arguements)

dict_response = post_codes.json()

# 1- Play around with API and getting data
# This prints out the keys in the get request
print(dict_response.keys())
#This prints out the status of the website (which inlcudes the URL and argument passed through)
print(dict_response['status'])
#This prints out the results as a dictionary
print(dict_response['result'])