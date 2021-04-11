import argparse
import requests
from requests.auth import HTTPBasicAuth
import os
import json

base_path = os.getcwd()

# Define the program description
text = 'This is a test program. It demonstrates how to use the argparse module with a program description.'

parser = argparse.ArgumentParser(description=text)

parser.add_argument("-V","--version",help="show program version",action="store_true")
parser.add_argument("username",help="Enter username",type=str)
parser.add_argument("password",help="Enter Password",type=str)
parser.add_argument("url",help="Enter Url",type=str)
parser.add_argument("payload",help="Enter Payload file name with extenstion",type=str)
parser.add_argument("-v","--verbs",help="Enter Method like GET,POST,defaul value is POST",default="POST")

args = parser.parse_args()
print(args)
raise SystemExit()

username = args.username
password = args.password
url = args.url
payload = args.payload
verbs  = args.verbs

file_name = os.path.join(base_path,args.payload)
print(file_name)

try:
    with open(file_name,'r') as fo:
        actual_payload = fo.read() 
except Exception as e:
    print("Error while fetching file:",e)
    raise SystemExit()

def call_rest_api(username,password,url,payload,verbs):    
    print("Url:",url,end="\n\n\n")
    print("Verbs:",verbs,end="\n\n\n")
    print('Request payload:\n\n',json.dumps(json.loads(payload),indent=4),end="\n\n\n")
    payload = json.loads(payload)
    headers = {
        # 'authorization': "Basic YWRtaW46MTIzNDU2",
        'content-type': 'application/json'
        }

    try:
        # response = requests.request(verbs, url, data=payload, headers=headers, auth=HTTPBasicAuth(username, password))
        if verbs=="POST":
            response = requests.post(url, json=payload, headers=headers, auth=HTTPBasicAuth(username, password))
        if verbs=="GET":
            response = requests.get(url,  json=payload, headers=headers, auth=HTTPBasicAuth(username, password))
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    print(response)
    if response.status_code != 200:
        print(response.text)
        print("Could not fetch order related to this RA number")
    else:
        return json.loads(response.text)


if args.version:
    print("my program version is 1.0")


response_payload = call_rest_api(username,password,url,actual_payload,verbs)
# print(response_payload)
print("Respnse Payload:\n\n",json.dumps(response_payload, indent=4))

raise SystemExit()





#cmd command 
#python argparser_python.py admin 123456 http://127.0.0.1:8880/api/device/get-hostname-by-vpn-id gethostnamebyvpnid.txtpi