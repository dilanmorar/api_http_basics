import requests

# build url
path_url = 'http://api.postcodes.io/postcodes/'
arguements = 'e146gt'

post_codes = requests.get(path_url+arguements)

print(post_codes)
print(type(post_codes))

# turn this into a dictionary
dict_response = post_codes.json()
print(dict_response)

# getting out data
print(dict_response.keys())
print(dict_response['status'])
print(dict_response['result'].keys())
print(dict_response['result']['longitude'])

for key in dict_response:
    print (key, ' ', dict_response['result'][key])