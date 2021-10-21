import os
from datetime import datetime
from datetime import date
from netmiko import ConnectHandler
import yaml


start_time = datetime.now()
today_date = str(date.today())

#Get yaml dict
with open('<devices yaml file>', 'r') as ymlfile:
    data = yaml.safe_load(ymlfile)

log_file = open('log_file.txt', "a")
log_file.write('--------------------START--------------------\n')
log_file.write('Date: ' + today_date + '\n')
log_file.write('Start Time: ' + (str(start_time))+ '\n')

#Connect
for device_index in data:
    
    device_name = device_index
    router = data.get(device_index)
      
    try:
        c = ConnectHandler(**router)        
        running_conf = c.send_command('show run')
        f = open('run_conf_'+ device_name +'_' + today_date + '.txt', "w")
        f.write(running_conf)        
        f.close()
        c.disconnect()
        work_status = device_name + ' Running Config Downloaded'
        log_file.write('Status: ' + work_status + '\n')
    except Exception as e:
        work_status = device_name + ' There is a problem with Config Downloading'
        log_file.write('Status: ' + str(e) + '\n')
        print(e) 
    
end_time = datetime.now()
total_time = str(end_time - start_time)

log_file.write('Total Time: ' + total_time + '\n')
log_file.close()

