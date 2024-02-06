# Standard Library Imports
import sys
import json

payload_dict = json.loads(sys.argv[0])

CSV_PATH = r'catalog.csv'

body = payload_dict["event"]["issue"]["body"]

test_payload = "### Contact Details\n\ncolin.bradshaw@paconsulting.com\n\n### What happened?\n\nThis is a test"

items = test_payload.split("###")
row = []

with open(CSV_PATH, 'a') as fin:
    fin.write(row)