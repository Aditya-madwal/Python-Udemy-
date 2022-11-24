# API parameters 
print("API parameters")

import requests

parameters = {
	"lat" : my_latitude,
	"lng" : my_longitude,
}

response = requests.get(url = "https://api.sunrise-sunset.org/json", params = paramters)

response.raise_for_status()

print(response) # prints <response [200]>
print(response.status_code) # prints 200

data = response.json()

print("done brather!")


