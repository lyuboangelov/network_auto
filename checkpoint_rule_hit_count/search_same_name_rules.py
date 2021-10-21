import json
import csv
import os
from pathlib import Path
import collections

file_path = Path("")
files = os.listdir(file_path)
list_from_rows_in_file = []

for file in files:
    f1 = open(file_path / file, 'r')    
    reader1 = csv.reader(f1, delimiter=",")
    print(file)
        
    for row_in_file in reader1:
        list_from_rows_in_file.append(row_in_file[1])    
    dict_items = collections.Counter(list_from_rows_in_file)
    dict_items_sorted = sorted(dict_items.items())

    for item in dict_items_sorted:
        if item[1] >= 2:
            print(item[0])    
    
    list_from_rows_in_file.clear()

  