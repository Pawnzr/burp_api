import requests
import json

API_KEY = ""
BASE_URL = "http://127.0.0.1"
SERVICE_PORT = "5555"
URI = BASE_URL+ ":" + SERVICE_PORT+ "/"+ API_KEY+ "/v0.1"

def get_issues():
    url = URI+"/knowledge_base/issue_definitions"
    res = requests.get(url, verify= False)
    
def launch_scan(target, username=None, password=None):
    url = URI + "/scan"
    data = {"urls": [target]}
    if username and password:
        data["application_logins"] = [
            {
                "username": username,
                "password": password,
                "type": "UsernameAndPasswordLogin"
            }
        ]

    response = requests.post(url, json=data)
    if response.status_code == 201:
        location_header = response.headers['Location']
        return location_header

def get_process(id: str):
    url = URI + f"/scan/{id}"
    res = requests.get(url, verify=False)
    return json.loads(res.text)["scan_metrics"]

def start_graphql():
    import requests

    url = "http://127.0.0.1:5555/graphql/v1"
    headers = {
        "Authorization": "",
        "Content-Type": "application/json"
    }

    data = {
        "query": "query GetSiteTree {\n  site_tree {\n    sites {\n      id\n      name\n      scope {\n        included_urls\n        excluded_urls\n      }\n      application_logins {\n        login_credentials {\n          label\n          username\n        }\n        recorded_logins {\n          label\n        }\n      }\n      parent_id\n      extensions {\n        id\n      }\n    }\n    folders {\n      id\n      name\n    }\n  }\n}",
        "operationName": "GetSiteTree"  
    }

    response = requests.post(url, json=data, headers=headers)

    print(response.status_code)
    print(response.json())
start_graphql()
