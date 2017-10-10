import requests
import sys
# URL = 'http://127.0.0.1:8000/'
# URL = 'http://127.0.0.1:8000/'
# URL = 'http://127.0.0.1:8000/'
# URL = 'http://127.0.0.1:8000/'
# http://localhost:8000/api/System_Administrator
# http://localhost:8000/api/Doctor
# http://localhost:8000/api/Nurse
# http://localhost:8000/api/Medical_Administrator
# http://localhost:8000/api/Insurance_Administrator
# http://localhost:8000/api/Patient
# http://localhost:8000/api/Record
# http://localhost:8000/api/Doctor_Exam_Record
# http://localhost:8000/api/Diagnosis_Record
# http://localhost:8000/api/Test_Results_Record
# http://localhost:8000/api/Insurance_Claim_Record
# http://localhost:8000/api/Patient_Doctor_Correspondence_Record
# http://localhost:8000/api/Raw_Record

## competition url
# http://172.17.0.2:8000/api/System_Administrator
# http://172.17.0.2:8000/api/Doctor
# http://172.17.0.2:8000/api/Nurse
# http://172.17.0.2:8000/api/Medical_Administrator
# http://172.17.0.2:8000/api/Insurance_Administrator
# http://172.17.0.2:8000/api/Patient
# http://172.17.0.2:8000/api/Record
# http://172.17.0.2:8000/api/Doctor_Exam_Record
# http://172.17.0.2:8000/api/Diagnosis_Record
# http://172.17.0.2:8000/api/Test_Results_Record
# http://172.17.0.2:8000/api/Insurance_Claim_Record
# http://172.17.0.2:8000/api/Patient_Doctor_Correspondence_Record
# http://172.17.0.2:8000/api/Raw_Record

function testytest(baseURL, port, route, uname, passw){
    
print(r.status_code, r.reason)
print(r.content.decode())

import requests

# URL = 'http://172.17.0.2:8000/'
URL = '{baseURL}:{port}/{route}'

payload = {
    'username': '{uname}',
    'password': '{passw}',
    }

session = requests.session()
r = requests.post(URL, data=payload)
print r.cookies
}

# function create{
# }
# function read{
# }
# function update{
# }
# function delete{
# }
print("enter deliminated by spaces: baseURL, port, route, username, passw")
function URL_builder(stdin, stdin, stdin, stdin, stdin){
