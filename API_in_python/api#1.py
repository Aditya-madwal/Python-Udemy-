# API (Application Programming Interface)
# Requests to be pulled from the internet and used by python

from textwrap import indent
import requests

response = requests.get(url = "http://api.open-notify.org/iss-now.json#")
print(response.raise_for_status())
print(response) # prints <request [200]>
print(response.status_code)

# raising an exception for certain conditions

if response.status_code == 401 :
    raise Exception("you are not authorized to access this data.")
elif response.status_code == 404 :
    raise Exception("that resourse does not exist.")

response.raise_for_status()
# if we dont get 'success' then the problem will automatiically be defined in the error (for eg - 404 = not found for url)

print(response.json())
# prints the json data as result 
# including lattitudes , longitudes and timestamp as int

print(response.json()["timestamp"])
# prints '5162536' the timestamp as 'int' only 

print(type(response.json()["timestamp"]))
# prints 'int'

print(response.json()['iss_position']["latitude"])
# prints the lattitudes as int
