import os
import pandas as pd


def convert_to_csv(path: str, file) -> None:
    """
    Converts file to csv file.
    Args:
        path: str, path where file is located.
        file: Dataframe to be converted.

    Returns: None

    """
    file.to_csv(path, index=False)


my_list = [item for item in range(1, 11)]
df = pd.DataFrame(my_list, columns=['Header'])
csv_path = os.path.join(fr'F:\python projects\json_files\file.csv')

convert_to_csv(csv_path, df)


trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk native vlan 999', 'switchport trunk allowed vlan', 'do not drink'
]

access_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

dict_to_csv = {'trunk': trunk_template, 'access': access_template}

df2 = pd.DataFrame(dict_to_csv)
csv_path2 = os.path.join(fr'F:\python projects\json_files\file2.csv')
convert_to_csv(csv_path2, df2)