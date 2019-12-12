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
print(f"longitude: {dict_response['result']['longitude']}")
print(f"latitude: dict_response['result']['latitude']")
print(f"nuts: dict_response['result']['nuts']")
print(f"admin_ward: dict_response['result']['admin_ward']")

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

# 5 - search a postcode and export data to a TXT file:

user_postcode = input('What is the postcode you would like to search for?')
path_url = 'http://api.postcodes.io/postcodes/'
result = requests.get(path_url + user_postcode.strip())
post_code_dict = result.json()
# ask for file creation name
ask_file = input('Please name the file you would like to insert your postcode data into')
file_name = ask_file + '.txt'
#create the file
try:
    with open(file_name, 'w+') as file_created:
            file_created.write(f"Postcode: {post_code_dict['result']['postcode']}."
                            f" Longitude: {post_code_dict['result']['longitude']}."
                            f" Latitude: {post_code_dict['result']['latitude']}."
                            f" Nuts: {post_code_dict['result']['nuts']}."
                            f" Admin Ward: {post_code_dict['result']['admin_ward']}.")
except TypeError as error:
    print('Invalid input')
finally:
    print('Completed')