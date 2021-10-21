import re
import json
from ipaddress import IPv4Network

search_regexes = {"name": "object\s*network\s*(?P<item>.*)", "description": "\s*description\s*(?P<item>.*)", "type": ['subnet', 'host', 'fqdn', 'range']}

def subnetmask_calculator(ip, mask):
    ip_and_mask = ip + "/" + mask
    net = IPv4Network(ip_and_mask)
    prefix = net.prefixlen
    return str(ip + "/" + str(prefix))

def clear_dict(d):
    d=dict((_, "") for _ in d)
    return d

def config_to_dict():
    item_dict = {
                    'name' : "",
                    "description": "",
                    'type': "",
                    'value': ""
                    }

    objects_dict = []
    
    config = open("config.txt", "r").readlines()

    for line in config: 
        for k, v in search_regexes.items():

            if k == "name" or k == "description":    
                regex = re.compile(v)
                text = regex.match(line)
                
                if text == None:
                    continue
                
                if k == "name": 
                    item_dict = clear_dict(item_dict)                                 
                    item_dict['name'] = text.group('item')                                                                        
                elif k == "description":
                    item_dict["description"] = text.group('item')
                    continue                    

            if k == "type":
                split_line = line.split()
                text = [i for i in split_line if i in v]
                if text:
                    item_dict['type'] = text[0]
                    if text[0] == v[0] or text[0] == v[3]:
                        item_dict['value'] = split_line[1] + " " + split_line[2]
                    elif text[0]:
                        item_dict['value'] = split_line[1]
                    continue
                break            
                               
                                    
            objects_dict.append(item_dict)        
    # payload_host = json.dumps([_ for _ in objects_dict], indent = 8) 
    return objects_dict

def payload_range():
    range_dict = {}
    range_objects = []    
    for i in config_to_dict():
        for k, v in i.items():
            if k == "type" and v == "range":
                range_dict["name"] = i["name"]
                range_ip = i["value"].split()
                range_network = range_ip[0] + "-" + range_ip[1]
                range_dict["value"] = range_network
                range_dict["type"] = "Range"           
                range_dict["description"] = i["description"]
                range_objects.append(range_dict) 
                range_dict = clear_dict(range_dict)                              

    return range_objects

def payload_host():
    host_objects = []
    for i in config_to_dict():
        for k, v in i.items():
            if k == "type" and v == "host":
                host_objects.append(i)
    return host_objects

def payload_fqdn():
    fqdn_dict = {}
    fqdn_objects = []    
    for i in config_to_dict():
        for k, v in i.items():
            if k == "type" and v == "fqdn":
                fqdn_dict["name"] = i["name"]                
                fqdn_dict["type"] = "FQDN"
                fqdn_dict["value"] = i["value"]
                fqdn_dict["dnsResolution"] = "IPV4_ONLY"
                fqdn_dict["description"] = i["description"]
                fqdn_objects.append(fqdn_dict) 
                fqdn_dict = clear_dict(fqdn_dict)                              

    return fqdn_objects
  
def payload_networks():
    network_dict = {}
    network_objects = []    
    for i in config_to_dict():
        for k, v in i.items():
            if k == "type" and v == "subnet":
                network_dict["name"] = i["name"]
                network_info = i["value"].split()
                network = subnetmask_calculator(network_info[0], network_info[1])
                network_dict["value"] = str(network)
                network_dict["overridable"] = "false"
                network_dict["description"] = i["description"]
                network_dict["type"] = "Network"
                network_objects.append(network_dict) 
                network_dict = clear_dict(network_dict)                              

    return network_objects

