import json
import csv
import os
from pathlib import Path


file_path = Path("")
files = os.listdir(file_path)


for f1 in files:
    for f2 in files:
        
        if f1 != f2:            
            f1_split = f1.split(" ")
            f2_split = f2.split(" ")

            if f1_split[0] == f2_split[0] and f1_split[1] == f2_split[1]:                
                file1 = open(file_path / f1, 'r')    
                reader1 = csv.reader(file1, delimiter=",")
                file2 = open(file_path / f2, 'r')    
                reader2 = csv.reader(file2, delimiter=",")

                for row_in_file1 in reader1:
                    for row_in_file2 in reader2:
                        if row_in_file1[1] == row_in_file2[1]:
                            hits_differnce = int(row_in_file2[2]) - int(row_in_file1[2])
                            if hits_differnce <= 0:
                                print(hits_differnce, row_in_file1[1])
                                pass
                            break
                            
                files.remove(f2)                
                break



        
            
            