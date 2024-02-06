# Standard Library Imports
import sys
import json

# Define constants
CATALOG_PATH = r'catalog/catalog.md'

'''
TODO: Deal with other use cases field:
    - Add function to take other use case and append to Use Cases Column values <----
    - List or display as it's own column?


TODO: Modify email address into a mailto link
'''

def transform_use_cases(insert_dict: dict) -> dict:
    use_cases_string = insert_dict['Covered Use Cases'].strip()

    use_cases_selected = [value.strip('- [X] ') for value in use_cases_string.split('\n') if "[X]" in value]

    insert_dict['Covered Use Cases'] = ', '.join(use_cases_selected)

    return insert_dict

def append_other_use_cases(insert_dict: dict) -> dict:
    use_cases = insert_dict['Covered Use Cases']
    other_use_case = insert_dict['Other Use Case']

    use_cases += ', ' + other_use_case

    insert_dict['Covered Use Cases'] = use_cases

    return insert_dict

def main():
    payload_dict = json.loads(sys.argv[1])

    body = payload_dict["event"]["issue"]["body"].split('###')[1:]

    insert_dict = {key:value for key, value in [item.strip().split('\n\n') for item in body]}

    del insert_dict['Confirm Submission?']

    transformed_insert_dict = transform_use_cases(insert_dict)

    retransformed_insert_dict = append_other_use_cases(transformed_insert_dict)

    del retransformed_insert_dict['Other Use Case']

    insert_list= list(transformed_insert_dict.values())

    insert_row = '| ' + ' | '.join(insert_list) + ' |'

    with open(CATALOG_PATH, 'r+') as fin:
        lines = fin.read()
        if lines[-1] in ['\n', '\r\n', '']:
            fin.write(insert_row)
        else: 
            fin.write('\n'+insert_row)

if __name__ == "__main__":
    main()