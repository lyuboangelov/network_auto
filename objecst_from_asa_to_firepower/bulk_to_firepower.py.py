import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
from asa_config_objects_to_dict import payload_range, payload_host, payload_fqdn, payload_networks
import urllib3

urllib3.disable_warnings()


address = input("Enter IP Address of the FMC: ")
username = input ("Enter Username: ")
password = getpass("Enter Password: ")


def check_response(returned_response):
    if returned_response.status_code == 201 or returned_response.status_code == 202:
        return print("Host Objects successfully pushed")
    else:
        return print("Host Object creation failed")

def login_and_generate_token(address, username, password):
    api_uri = "/api/fmc_platform/v1/auth/generatetoken"
    url = "https://" + address + api_uri
    response = requests.request("POST", url, verify=False, auth=HTTPBasicAuth(username, password))
    accesstoken = response.headers["X-auth-access-token"]
    refreshtoken = response.headers["X-auth-refresh-token"]
    DOMAIN_UUID = response.headers["DOMAIN_UUID"]
    return [accesstoken, refreshtoken, DOMAIN_UUID];

def bulk_objects(objects_list, adress, login, obj_type):
        host_api_uri = "/api/fmc_config/v1/domain/" + login[2] + "/object/" + obj_type + "?bulk=true"
        host_url = "https://" + address + host_api_uri
        headers = { 'Content-Type': 'application/json', 'x-auth-access-token': login[0]}
        response = requests.request("POST", host_url, headers=headers, json=objects_list, verify=False)
        return response



# login_to_fmc = login_and_generate_token(address, username, password)


