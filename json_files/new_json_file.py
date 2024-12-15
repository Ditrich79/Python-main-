import os
import json

def convert_json_file(path: str, file: list[dict[str, list[int]|list[str]]]) -> None:
    """
    This function converts text files into new json file.
    :param path: file path
    :param file: file list that need to be converted
    :return: None
    """
    with open(path, "w", encoding="utf-8") as js_file:
        js_file.write(json.dumps(file, indent=2))


file_path_raw = os.path.join(rf'F:\python projects\json_files', 'written_json_2.json')

data = [item for item in range(1, 11)]

data2 = ['one', 'two', 'three', 'four', 'fife', 'six', 'seven', 'eight', 'nine', 'ten']

dictionary = [
    {'numbers': data, 'words': data2}
]

convert_json_file(file_path_raw, dictionary)
