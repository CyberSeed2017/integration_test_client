import requests
import json

base_url = 'http://127.0.0.1:8000/api/'
auth = ('Admin', 'Mike_Knows')
headers = {
    'content-type': "application/json",
    'authorization': "Basic YWRtaW46TGV0TWVJbkBVTkY=",
    'cache-control': "no-cache",
    'postman-token': "238fb322-0835-a734-a176-5b5621261a0f"
}

def insert(payload, service):
    url = base_url + service
    #payload = {'some': 'data'}
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers, allow_redirects=False, auth=auth)
    #print(response)
    location = response.headers['Location']
    print(location)
    return location

def g(resource_uri):
    response = requests.get("http://127.0.0.1:8000" + resource_uri, auth=auth)
    data = response.json()
    print (data)
    print data['id']
#

### INTEGRATION TEST SCENARIOS ###

#1 /createUser
payload = {"first_name": "Ahmed", "is_staff": True, "last_name": "Moussa", "password": "3e06434338085d2ddf6ddcde204101f0", "username": "admin11", "groups" : ["/api/Group/2/",]}
uri = insert(payload, "User/")
g(uri)

#2 /createDoctor
payload = {"Practice_Address": "Taylor", "Practice_Name": "Taylor","Recovery_Phrase": "Taylor", "username": "/api/User/3/"}
uri = insert(payload, "Doctor/")
g(uri)


#1 /createNurse
payload = {"Practice_Address": "Nurse", "Practice_Name": "Taylor","Recovery_Phrase": "Taylor", "username": "/api/User/3/", "Associated_Doctors": ["/api/Doctor/26/", "/api/Doctor/29/"],}
uri = insert(payload, "Nurse/")
g(uri)

    

