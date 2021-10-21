from datetime import datetime
from datetime import date
from netmiko import ConnectHandler
import yaml
import re

start_time = datetime.now()
today_date = str(date.today())
print(start_time)

### Enter MAC ADDRESS BELOW IN FORMAT xxxx.xxxx.xxxx ###
MAC_ADDRESS = ""

port_regex = re.compile("Fa|Gi")
regex = re.compile(MAC_ADDRESS)

#Get yaml dict
with open('devices.yml', 'r') as ymlfile:
    data = yaml.safe_load(ymlfile)

#Connect
for device_index in data:
    
    device_name = device_index
    router = data.get(device_index)
      
    try:
        c = ConnectHandler(**router)               
        mac_table = c.send_command('show mac address-table address ' + MAC_ADDRESS)
        mac_table = mac_table.split("\n")
        for line in mac_table:            
            if regex.findall(line):
                if port_regex.findall(line):                
                    print(router["ip"])
                    print(line)              
        c.disconnect()
        
    except Exception as e:
        work_status = device_name + 'Cant find MAC ADRESS'        
        print(e) 
    
end_time = datetime.now()
total_time = str(end_time - start_time)
print(end_time)
print(total_time)

