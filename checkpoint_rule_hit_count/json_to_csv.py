import json
import csv

from pathlib import Path


file_path_json = Path("")
file_path_csv = Path("")



policies = []

for policy in policies:
    filename = file_path_json / policy + ".json"
    f = open(filename)
    text_file = policy +"txt.txt"
    new_file = open(text_file, "a")
    text = json.load(f)

    no_name = 0

for r in text:
    for i in r['rulebase']:        
        for j in i['rulebase']:

            try:             
               name = (i['rulebase'][(int(j['rule-number'] - 1))]["name"])                
            except KeyError:
                no_name += 1
                name = ("No_Name_" + str(no_name))

            try:
                hits = str((j['hits']['value']))
            except KeyError:
                hits = "NO_HITS"
            rule_number = str((j['rule-number']))                           
                            
            info_to_write = (str(name) + "," + str(rule_number) + "," + str(hits) + "\n")
            new_file.write(info_to_write)
            
    new_file.close()
    f.close()    
            
    