import requests
from requests.auth import HTTPBasicAuth

#API Info
#access_token = "X-RapidAPI-Key" : "25649f62f2msh3808137a2442080p186039jsn6c56c32c82f1"
API_Add = 'https://adsbexchange-com1.p.rapidapi.com/v2/lat/27.943721/lon/-82.537932/dist/5/'
#API_Host = "X-RapidAPI-Host": "adsbexchange-com1.p.rapidapi.com"
headers = {	"X-RapidAPI-Key" : "25649f62f2msh3808137a2442080p186039jsn6c56c32c82f1",	"X-RapidAPI-Host" : "adsbexchange-com1.p.rapidapi.com"}


# Make the request to the API
response = requests.get(API_Add, headers=headers)
print(response)

if response.status_code == 401:    
    response = requests.get(API_Add)
else:
    response.status_code == 200
    # The request was successful, so parse the response data
    print("API Call Successful")
    data = response.json()

print(data)