import json
import os
import pandas as pd


def pack_json(array, path):
    with open(path, 'w') as file:
        file.write(json.dumps(array))


trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
]

access_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

to_json = {'trunk': trunk_template, 'access': access_template}

file_path = os.path.join(rf'F:\python projects\json_files', rf'written_js.json')
pack_json(to_json, file_path)

with open(r'F:\python projects\json_files\written_js.json', 'r') as read_file:
    print(read_file.read())

