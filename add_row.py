# Standard Library Imports
import sys
import json

payload_dict = {}

print(f'test file inserted is {sys.argv[1]}')

with open(sys.argv[1]) as fin:
    payload_dict = json.load(fin)

CSV_PATH = r'catalog.csv'

body = payload_dict["event"]["issue"]["body"].split('###')[1:]

insert_dict = {key:value for key, value in [item.strip().split('\n\n') for item in body]}

insert_list= list(insert_dict.values())

insert_row = ','.join(f'"{record}"' for record in insert_list)

with open(CSV_PATH, 'a') as fin:
    fin.write(insert_row+'\n')