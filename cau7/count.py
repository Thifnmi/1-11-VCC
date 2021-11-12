import os
import csv
# print(len(os.listdir(os.getcwd()+"/result_Process")))
for filename in os.listdir(os.getcwd()+"/result_Process"):
    print(filename)
    with open(os.path.join(os.getcwd()+"/result_Process", filename), 'r', encoding='utf-8') as f:
        reader = f.readlines()
        row = reader[1:]
        print((row[0]))
        # for row in reader:
        #     print(row[2])
