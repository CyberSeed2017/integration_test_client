import requests
import json

URL = 'http://127.0.0.1:8000/api/'

def insert(payload):
    url = 'http://127.0.0.1:8000/api/Doctor/'
    #payload = {'some': 'data'}
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, allow_redirects=False)
    #print(response)
    location = response.headers['Location']
    print(location)
    g(location)

    
    '''
    print(response.request.body)
    print(response.request.headers)
    for resp in response.history:
        print resp.status_code, resp.url
    '''
    

def g(resource_uri):
    response = requests.get("http://127.0.0.1:8000" + resource_uri)
    data = response.json()
    print (data)
    print data['id']
    #print(response)
#

#create a doctor
jsonData = {"Practice_Address": "UNF4", "Practice_Name": "Moussa4","Recovery_Phrase": "Test4"}
insert(jsonData)

#data = json.loads(jsonData)
#req.add_header('Content-Type', 'application/xml; charset=utf-8')
#r = requests.post(URL + "Doctor/", data, headers='{"content-type": "application/json"}')

#print(r)

#print(r.status_code, r.reason)
    
