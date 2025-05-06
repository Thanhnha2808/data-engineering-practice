import os
import json
import csv
from glob import glob

def flatten_json(y):
    """Làm phẳng JSON lồng nhau"""
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], f'{name}{a}_')
        elif type(x) is list:
            for i, a in enumerate(x):
                flatten(a, f'{name}{i}_')
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

def convert_json_to_csv(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if isinstance(data, dict):
        data = [data]

    flat_data = [flatten_json(item) for item in data]
    csv_file = json_file.replace('.json', '.csv')

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=flat_data[0].keys())
        writer.writeheader()
        writer.writerows(flat_data)

def main():
    base_dir = os.path.dirname(__file__) if '__file__' in globals() else os.getcwd()
    data_dir = os.path.join(base_dir, 'data')
    json_files = glob(os.path.join(data_dir, '**', '*.json'), recursive=True)

    for json_file in json_files:
        print(f"Converting: {json_file}")
        convert_json_to_csv(json_file)

if __name__ == "__main__":
    main()
