import requests
import json

base_url = 'http://127.0.0.1:8000/api/'

def insert(payload, service):
    url = base_url + service'
    #payload = {'some': 'data'}
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, allow_redirects=False)
    #print(response)
    location = response.headers['Location']
    print(location)
    return location

def g(resource_uri):
    response = requests.get("http://127.0.0.1:8000" + resource_uri)
    data = response.json()
    print (data)
    print data['id']
#

### INTEGRATION TEST SCENARIOS ###

#1 /createDoctor
payload = {"Practice_Address": "Taylor", "Practice_Name": "Taylor","Recovery_Phrase": "Taylor"}
loc = insert(payload, "Doctor/")
g(location)

    
