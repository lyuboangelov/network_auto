import requests, json
from pathlib import Path

file_path = Path("")

policies = []


def api_call(ip_addr, port, command, json_payload, sid):
    url = 'https://' + ip_addr + ':' + port + '/web_api/' + command
    if sid == '':
        request_headers = {'Content-Type' : 'application/json'}
    else:
        request_headers = {'Content-Type' : 'application/json', 'X-chkp-sid' : sid}
    r = requests.post(url,data=json.dumps(json_payload), headers=request_headers, verify=False)
    return r.json()


def login(user,password):
    payload = {'user':user, 'password' : password}
    response = api_call('', '443', 'login', payload, '')
    return response["sid"]

sid = login('','')
print("session id: " + sid)

for policy in policies:
    
    payload = {
    "offset" : 0,
    "limit" : 500,
    "details-level" : "standard",
    "name" : policy,  
    "use-object-dictionary" : 'true',
    "show-hits" : 'true'
    }
    
    rulebase_results = api_call('', '443', 'show-access-rulebase', payload, sid)
    text = json.dumps(rulebase_results, indent=2)
    filename = policy + ".json"
    f = open(file_path / filename, "a")
    f.write(text)
    f.close()

logout = api_call('', '443',"logout", {}, sid)

# new_host_data = {'name':'', 'ip-address':''}
# new_host_result = api_call('', 443,'add-host', new_host_data ,sid)
# print(json.dumps(new_host_result))

# publish_result = api_call('', 443,"publish", {},sid)
# print("publish result: " + json.dumps(publish_result))

# logout_result = api_call('', 443,"logout", {},sid)
# print("logout result: " + json.dumps(logout_result))	