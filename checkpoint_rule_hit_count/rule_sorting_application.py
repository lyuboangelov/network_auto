import json
import csv
from pathlib import Path


file_path_json = Path("")
file_path_csv = Path("")

policies = []


for policy in policies:
    filename_json = file_path_json / (policy + ".json")
    json_file = open(filename_json)
    filename_csv = file_path_csv / (policy + " .csv")
    new_csv_file = open(filename_csv, "a")
    data = json.load(json_file)

    no_name = 0


    for key in data['rulebase']:    
        rule_number = str(key['rule-number'])
        hits = str(key['hits']['value'])
        try:
            rule_name = str(key['name'])
        except KeyError:
            no_name += 1
            rule_name = "Without_Name_" + str(no_name)
        
        
        info_to_write = (rule_number + "," + rule_name + "," + hits + "\n")
        new_csv_file.write(info_to_write)
    new_csv_file.close()
    json_file.close() 